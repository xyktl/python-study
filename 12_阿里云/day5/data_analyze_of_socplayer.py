# -*- coding: utf-8 -*-
# 1.导入分析所需要用到的库。
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
#player.info()

# 4.对数据可能的异常值与重复值进行检测。
# player.describe()  #查看异常值
player.duplicated().any()  # 检查是否有重复值
player.drop_duplicates(inplace=True)  # 去除重复值


# 5.将身高体重进行类型转换，并显示关于身高，体重与评分的核密度图。
player["Height"] = player["Height"].map(lambda x: str(x).replace("cm", ""))
player["Weight"] = player["Weight"].map(lambda x: str(x).replace("kg", ""))
player[["Height", "Weight", "Rating"]].plot(kind="kde")
# 6.显示左脚与右脚球员的比例。
# 7.从俱乐部与国家队的角度，统计评分数据top10的俱乐部/ 国家（人数需要超过20人）。
# 8.分析拥有更忠心球员的俱乐部。在俱乐部踢球 >= 5 year
# 9.足球运动员是否与出生月份相关？
# 10.球衣号码与位置是否相关。
# 11.身高与体重是否存在线性关系？
# 12.那些技能（指标）对评分的影响较大？
# 13.对最后两列所表示的技能类型进行分析（假设不知道最后两列表示的是什么技能）
# 14.分析年龄与评分之间，是否具有一定关联性。
