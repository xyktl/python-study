# -*- coding: utf-8 -*-

# 1.导入分析所需要用到的库。

#分析文件 足球运动员 r"c:\Users\Hasse\Desktop\FullData.csv"
import numpy
import pandas
import matplotlib
from matplotlib import pyplot
matplotlib.rcParams["font.family"] = "SimHei"
matplotlib.rcParams["axes.unicode_minus"] = False


#  2.加载并显示数据集，同时设置最大显示的列数。

player = pandas.read_csv(r"c:\Users\Hasse\Desktop\FullData.csv")    # 加载数据
pandas.set_option("max_columns", 100)   # 设置展示的最大列数
player.head()  # 显示数据

#  3.过滤数据集中的控制，并显示数据集的信息。
# 对数据进行简单的处理查看
# player.info() #查看缺失信息（以及每列的类型信息）
player = player[player["Club_Position"].notnull()]  # 补全缺失信息
# player.info()

# 4.对数据可能的异常值与重复值进行检测。
# player.describe()  #查看异常值
player.duplicated().any()  # 检查是否有重复值
player.drop_duplicates(inplace=True)  # 去除重复值


# 5.将身高体重进行类型转换，并显示关于身高，体重与评分的核密度图。
player["Height"] = player["Height"].map(lambda x: str(x).replace("cm", ""))
player["Weight"] = player["Weight"].map(lambda x: str(x).replace("kg", ""))
player[["Height", "Weight", "Rating"]].plot(kind="kde")
# 6.显示左脚与右脚球员的比例

# 左脚与右脚选手在数量上的偏差。
# player["Preffered_Foot"].value_counts()
# 画图展示
player["Preffered_Foot"].value_counts().plot(kind="bar")

# 7.从俱乐部与国家队的角度，统计评分数据top10的俱乐部/ 国家（人数需要超过20人）。

# 从俱乐部的角度分析
# s = player.groupby("Club")["Rating"].agg(["count", "sum", "mean"])
# s = s[s["count"] > 20]
# s.sort_values("count", ascending=False)
# s.sort_values("mean", ascending=False)
# 从国家的角度分析
s = player.groupby("Nationality")["Rating"].agg(["count", "sum", "mean"])
s = s[s["count"] > 20]
s.sort_values("mean", ascending=False).head(10)

# 8.分析拥有更忠心球员的俱乐部。在俱乐部踢球 >= 5 year

# 获取加入俱乐部的年份
year = player["Club_Joining"].map(lambda x: str(x).split("/")[-1])
# 目前，这个年份还是字符串类型的，我们需要转换为数值（整数）类型
year = year.astype(numpy.int)
t = player[(2017 - year >= 5) & (player["Club"] != "Free Agents")]
t["Club"].value_counts().head(10).plot(kind="bar")

# 9.足球运动员是否与出生月份相关？

# 1 全体运动员
# 2 知名运动员（80分及以上）
t = player[player["Rating"] >= 80]
t = t["Birth_Date"].str.split("/", expand=True)
# 全体运动员
# t = player["Birth_Date"].str.split("/", expand=True)
t[0].value_counts().plot(kind="bar")

# 10.球衣号码与位置是否相关。

# 去除替补球员与后备队球员。
t = player[(player["Club_Position"] != "Sub") & (player["Club_Position"] != "Res")]
x = t.groupby(["Club_Kit", "Club_Position"]).size()
x[x > 50].plot(kind="bar")

# 11.身高与体重是否存在线性关系？

# 身高与体重是否具有相关性？

# 将 Height Weight 对应的数据转换为整形
player["Height"] = player["Height"].map(lambda x: int(x))
player["Weight"] = player["Weight"].map(lambda x: int(x))
player.plot.scatter(x="Height", y="Weight")

# 12.那些技能（指标）对评分的影响较大？

# 查看player的相关系数。
player.corr()

# 13.对最后两列所表示的技能类型进行分析（假设不知道最后两列表示的是什么技能）

# 假设我们不清楚后两列的具体含义是什么，分析该标题可能的含义？
# player.info()
# 对位置进行分组
g = player.groupby("Club_Position")
g["GK_Positioning"].agg("mean").plot(kind="bar")

# 14.分析年龄与评分之间，是否具有一定关联性。

# 年龄与评分具有怎样的关系？
t = player[["Age", "Rating"]]
t["Age"] = pandas.cut(player["Age"], bins=[0, 20, 30, 40, 100], labels=["小", "中", "大", "很大"])
t.groupby("Age")["Rating"].mean().plot(kind="line", xticks=[0, 1, 2, 3, 4], marker="o")
