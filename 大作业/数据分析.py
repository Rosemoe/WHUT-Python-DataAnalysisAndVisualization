# 附件中已带data/data.csv。如未生成data/data.csv，请先运行数据爬取，再运行数据分析
import pandas as pd
from pandas import DataFrame
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re, tqdm
from wordcloud import WordCloud

# 所有动画类型标签
anime_sorts = '热血 冒险 搞笑 运动 竞技 剧情 穿越 青春 小说改 游戏改 轻小说改 漫画改 漫改 轻改 GAL改 后宫 校园 离职 恋爱 爱情 百合 耽美 战斗 机战 科幻 萝莉 奇幻 特摄 魔法 动画 治愈 美食 萌系 偶像 泡面 催泪 日常 音乐 少女 社团 推理 乙女 异世界 恐怖 猎奇'.split()

# 统一动画类型标签
def replace_tag(x):
    replacements = {
        '漫改': '漫画改', '轻改': '小说改', '轻小说改':'小说改', '轻百合':'百合',
        '游改':'游戏改', 'GAL改': '游戏改', '泡面番': '泡面'
    }
    if x in replacements:
        return replacements[x]
    return x

# 统一播出时间格式
def replace_day(x):
    days = ['一', '二', '三', '四', '五', '六', '日']
    x = x.replace('星期', '').strip()
    if x in days:
        return x
    elif re.fullmatch('[1-7]', x):
        return days[int(x) - 1]
    else:
        return '其他'

# 统计播出时间在星期几的动画数量
def plot_day(df: DataFrame):
    df['day_uniformed'] = df.loc[:,'day'].apply(replace_day) # 替换播出时间，使之格式统一
    df.groupby('day_uniformed').size().sort_values(ascending=False).plot(kind='bar', title='播出时间在星期几的动画数量')
    plt.xlabel('星期')
    plt.ylabel('数量')
    plt.savefig('播出时间统计.png')

# 绘制标签词云图
def plot_wordcloud(df: DataFrame):
    tags_column = df[0:500]['tags'] # 取前500个动画
    tags_column = tags_column.dropna() # 去除标签缺失的值
    freq = {}
    transform = lambda lst: set([replace_tag(x) for x in lst]) # 替换标签，避免同类标签有多种写法
    for tags in tags_column:
        for tag in transform(eval(tags)): # eval函数将字符串转换为列表
            if re.search('[0-9]+', tag): # 忽略含有数字的标签
                continue
            if tag in freq:
                freq[tag] += 1
            else:
                freq[tag] = 1
    wdcld = WordCloud(font_path='C:\\Windows\\Fonts\\simkai.ttf', width=1000, height=618, background_color='white', relative_scaling=0.5)
    wdcld.generate_from_frequencies(freq).to_file('标签词云.png') # 生成词云图

# 绘制排名与分数、抛弃率的散点图，以及线性拟合曲线
def plot_mark_relation(df: DataFrame):
    df = df[df['rank'] <= 2000].copy() # 取排名前2000的动画
    df['abandon_rate'] = df['abandoned'] / (df['watching'] + df['on_hold'] + df['completed'] + df['plan_to_watch'] + df['abandoned']) # 计算抛弃率
    # 使用 Numpy 线性拟合散点
    def linear_fit(x, y):
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        plt.plot(x, p(x), color='red') # 绘制线性拟合曲线
    x, y = df['rank'].values, df['score'].values
    df.plot.scatter(x='rank', y='score', title='排名与分数的散点图', figsize=(15, 10), fontsize=17) # 绘制排名与分数的散点图
    linear_fit(x, y)
    plt.xlabel('排名', fontsize=17)
    plt.ylabel('分数', fontsize=17)
    plt.savefig('排名与分数的散点图.png')
    y = df['abandon_rate'].values
    df.plot.scatter(x='rank', y='abandon_rate', title='排名与抛弃率的散点图', figsize=(15, 10), fontsize=17) # 绘制排名与抛弃率的散点图
    linear_fit(x, y)
    plt.xlabel('排名', fontsize=17)
    plt.ylabel('抛弃率', fontsize=17)
    for idx in df.index.values:
        if df.loc[idx, 'abandon_rate'] > 0.2:
            print(df.loc[idx,:])
    plt.savefig('排名与抛弃率的散点图.png')

# 绘制动漫话数的饼图
def plot_episode(df: DataFrame):
    data = df['episode_cnt']
    # 筛选为数字的区域
    data = data[data.apply(lambda x: re.fullmatch('[0-9]+', x) is not None)]
    data = data.apply(lambda x: x if int(x) <= 50 else '50+') # 合并50话以上的动画
    res = data.value_counts()
    sum = res.sum()
    # 合并占比小于1%的数据
    res = res[res / sum >= 0.01]
    res['其他'] = sum - res.sum()
    plt.ylabel('')
    # 显示百分比和名称
    plt.pie(res, labels=res.index, autopct='%1.1f%%', pctdistance=0.8, labeldistance=1.1, textprops={'fontsize': 17})
    plt.savefig('动漫话数占比的饼图.png')

# 绘制动画类型的趋势年份图
def plot_trending(df: DataFrame):
    df = df.dropna(subset=['tags']).copy()
    stop_tags = '小说改 游戏改 轻小说改 漫画改 漫改 轻改 GAL改'.split()
    def determine_type(lst): # 确定动画类型
        for sort in anime_sorts:
            if sort in lst and sort not in stop_tags:
                return sort
        for sort in anime_sorts:
            if sort in lst:
                return sort
        return '其他'
    df['sort'] = df['tags'].apply(lambda x:determine_type(eval(x))) # 提取动画类型
    df['sort_uniformed'] = df['sort'].apply(replace_tag) # 替换动画类型，避免同类动画类型有多种写法
    df = df.groupby('year')['sort_uniformed'].value_counts() # 统计每年每种动画类型的数量
    # 除去sort_uniformed为其他的值
    df = df[df.index.get_level_values('sort_uniformed') != '其他']
    df.unstack().fillna(0).plot(title='动画类型的趋势年份图', kind='line', figsize=(15, 10), fontsize=15) # 绘制折线图
    plt.xlabel('年份')
    plt.xticks(range(2000, 2024))
    plt.ylabel('数量')
    plt.legend(loc=3, bbox_to_anchor=(1, 0), borderaxespad=0)
    plt.savefig('动画类型的趋势年份图.png')

if __name__=='__main__':
    plt.rcParams['font.family'] = [ 'SimHei' ] # 指定默认字体为黑体
    sns.set_theme(font='SimHei', style='whitegrid', font_scale=1.1) # 设置seaborn主题为白色网格
    df = pd.read_csv('data/data.csv', encoding='utf-8') # 读取数据
    df = df.dropna(subset=['day', 'time']).copy() # 去除时间缺失的值
    df['year'] = df['time'].apply(lambda x: int(re.search('[0-9]+', x).group())) # 提取年份
    df = df[df['year'] >= 2000].copy() # 只保留2000年以后的动画，2000年以前的动画数量太少，参考价值较低
    df['episode_cnt'] = df['episode_cnt'].apply(lambda x: x.strip())
    # 逐个调用处理函数，绘制图像
    targets = [plot_day, plot_wordcloud, plot_trending, plot_mark_relation, plot_episode]
    for target in tqdm.tqdm(targets, desc='处理数据'):
        target(df)
        plt.clf()