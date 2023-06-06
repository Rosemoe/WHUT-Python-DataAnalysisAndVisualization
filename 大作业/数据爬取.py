# 爬取所有页面数据需要约40分钟（可中断），生成CSV文件（位于data/data.csv）需要约5分钟
import requests, pickle, os, tqdm, threading, re
from fake_useragent import UserAgent
import pandas as pd
from bs4 import BeautifulSoup

page_limit = 321 # 爬取的排行榜页面数量（Bangumi上只有321页）
threading_num = 6 # 爬取详情页的线程数量

# 生成请求头
def gen_headers(): 
    return {
        'User-Agent': UserAgent().random,
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }

# 爬取bangumi.tv的排行榜数据
def fecth_ranking_data():
    for i in tqdm.trange(page_limit, desc='爬取排行榜', unit='page'):
        # 跳过已经爬取过的页面
        if os.path.exists('data/page_{}.pkl'.format(i + 1)):
            continue
        results = []
        url = 'https://bangumi.tv/anime/browser?sort=rank&page=' + str(i+1)
        response = requests.get(url, headers=gen_headers())
        response.encoding = 'utf-8'
        soup =  BeautifulSoup(response.text, 'lxml')
        items = soup.find('ul', class_='browserFull').find_all('li')
        for item in items:
            content = item.find('div', class_='inner')
            name, name_jp = content.find('a', class_='l').text, content.find('h3').small
            # 获取每部动漫的排名和评分信息
            info = {
                'name': name,
                'name_jp': name_jp.text if name_jp else name,
                'url': 'https://bangumi.tv' + item.find('a', class_='subjectCover cover ll').get('href'),
                'rank': int(content.find('span', class_='rank').text.replace('Rank ', '')),
                'score': float(content.find('small', class_='fade').text),
                'participants': int(content.find('span', class_='tip_j').text.replace('人评分', '')[1:-1]),
            }
            results.append(info)
        pickle.dump(results, open('data/page_{}.pkl'.format(i + 1), 'wb')) #保存一页的数据

# 合并排行榜的各个页面
def merge_ranking_data():
    results = []
    for i in tqdm.trange(page_limit, desc='合并排行榜', unit='file'):
        results += pickle.load(open('data/page_{}.pkl'.format(i + 1), 'rb'))
    pickle.dump(results, open('data/ranking.pkl', 'wb'))

# 使用多线程爬取各个动漫的详情页，并暂存到本地(约7700个页面)
def fetch_details():
    items = pickle.load(open('data/ranking.pkl', 'rb'))
    candidates = tqdm.trange(len(items), desc='爬取详情页', unit='item')
    itr, lock = candidates.__iter__(), threading.Lock()
    def exec(): # 爬取详情页的函数
        while True:
            try:
                lock.acquire(True) #加锁处理
                idx = next(itr)
            except Exception as e:
                if type(e) != StopIteration:
                    print(e)
                break
            finally:
                lock.release()
            item = items[idx]
            idx = idx + 1
            if os.path.exists('data/details_{}.pkl'.format(idx)):
                continue
            pickle.dump(requests.get(item['url'], headers=gen_headers()), open('data/details_{}.pkl'.format(idx), 'wb'))
    # 创建线程并加入等待完成
    threads = [(lambda x: (lambda i,j: i)(x, x.start()))(threading.Thread(target=exec)) for k in range(threading_num)]
    for t in threads:
        t.join()

# 将爬取的数据关联到排名榜单
def link_details():
    if os.path.exists('data/data.pkl'):
        return pickle.load(open('data/data.pkl', 'rb'))
    items = pickle.load(open('data/ranking.pkl', 'rb'))
    failure_cnt = 0
    for i in tqdm.trange(len(items), desc='关联详情页', unit='item'):
        idx = i + 1
        if os.path.exists('data/details_{}.pkl'.format(idx)):
            try:
                details = pickle.load(open('data/details_{}.pkl'.format(idx), 'rb'))
                details.encoding = 'utf-8'
                text = details.text
                soup = BeautifulSoup(text, 'lxml')
                # 获取动漫的各种信息(标签、制作公司、放送时间、放送星期、话数)
                tags_containers = soup.find('div', id='columnSubjectHomeB').find('div', class_='subject_tag_section').find_all('a', class_='l')
                items[i]['tags'] = [tag.find('span').text for tag in tags_containers if tag.find('small').text != '更多 +' and int(tag.find('small').text) > 25] # 只保留出现次数大于25的标签
                info_map = {item[0] : item[1] for item in list(map(lambda x:x.text.split(':'), soup.find('div', id='columnSubjectHomeA').find('ul', id='infobox').find_all('li')))}
                items[i]['maker'], items[i]['time'], items[i]['day'], items[i]['episode_cnt'] = info_map.get('动画制作', ''), info_map.get('放送开始', ''), info_map.get('放送星期', ''), info_map.get('话数', '')
                type_names, suffixes = ['watching', 'abandoned', 'completed', 'on_hold', 'plan_to_watch'], ['在看', '抛弃', '看过', '搁置', '想看']
                # 获取动漫的各种状态下的人数
                for type_name, suffix in zip(type_names, suffixes):
                    res = re.search(r'(\d+)人{}'.format(suffix), text)
                    items[i][type_name] = 0 if res == None else int(res.group(1))
            except Exception as e:
                failure_cnt += 1
                if str(e) != "'NoneType' object has no attribute 'find'":
                    print('解析第{}项时出错：{}'.format(idx, e))
    print('{}个项目存在数据丢失情况'.format(failure_cnt))
    result = list(filter(lambda x: 'tags' in x, items)) # 只保留解析成功的动漫
    pickle.dump(result, open('data/data.pkl', 'wb'))
    return result

# 执行入口
if __name__=='__main__':
    if not os.path.exists('data'):
        os.mkdir('data')
    if not os.path.exists('data/data.pkl'):
        print('正在爬取数据')
        fecth_ranking_data()
        merge_ranking_data()
        fetch_details()
    print('正在解析数据')
    details = link_details()
    print('正在生成CSV文件')
    # 保存到csv文件
    df = pd.DataFrame(details)
    df.to_csv('data/data.csv', index=False, encoding='utf-8')
    print('CSV文件已生成')