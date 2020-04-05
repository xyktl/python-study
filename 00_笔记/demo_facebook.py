# -*- coding: utf-8 -*-


#1.导入运行所必须的库。

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
#②定义load_data函数，用于加载数据集，并对数据集进行预处理。返回处理之后的结果。

def load_data(path):
    """加载数据集，并对数据集进行处理。
    
    Parameters
    -----
    path : str
        数据集的路径。
        
    Returns
    -----
    (X, y) : tuple
        特征矩阵X与对应的标签y。
    """
    
    # 加载数据集，注意数据集中没有标题行，需要将header的值设置为None。
    data = pd.read_csv(path, header=None)
    # 将加载的数据集分为特征X与标签y。
    X, y = data.iloc[:, :-1], data.iloc[:, -1]
    # 对特征矩阵X进行编码。
    lb = LabelEncoder()
    X = X.apply(lambda col: lb.fit_transform(col))
    # 进行one-hot编码
    ohe = OneHotEncoder()
    X = pd.DataFrame(ohe.fit_transform(X).toarray())
    # tensorflow不支持数值列，需要转换。
    X.columns = X.columns.map(lambda x: f"c{x}")
    return X, y
#③定义train_input_fn函数，用于构建训练集。

def train_input_fn(features, labels):
    """定义训练函数，用于训练使用。
    
    Parameters
    -----
    features : 类数组类型。 形状：[样本数量， 特征数量]
        用于训练的特征矩阵。
    labels : 类数组类型。形状为：[样本数量]
        每个样本对应的标签。（分类）
        
    Returns
    -----
    dataset : tf.data.Dataset
        数据集。
    """
    
    # 创建数据集
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
    # 对数据集进行洗牌，重复与分批处理。
    dataset = dataset.shuffle(10000, seed=0).repeat(10).batch(50)
    return dataset
#4.定义eval_input_fn评估函数，用于评估模型效果，或对新数据进行预测。

def eval_input_fn(features, labels=None):
    """定义评估函数，用于评估或预测。
    
    Parameters
    -----
    features : 类数组类型。 形状：[样本数量， 特征数量]
        用于测试的特征矩阵。
    labels : 类数组类型。形状为：[样本数量]
        每个样本对应的标签。（分类）
        
    Returns
    -----
    dataset : tf.data.Dataset
        数据集。
    """
    # 将特征转换成字典类型
    features = dict(features)
    # 如果要进行未知数据的预测，则没有标签。
    if labels is None:
        inputs = features
    else:
        inputs = (features, labels)
    # 创建数据集
    dataset = tf.data.Dataset.from_tensor_slices(inputs)
    # 每次取出100条记录
    dataset = dataset.batch(100)
    return dataset
#5.加载数据集，定义DNNClassifier类，对模型进行训练，并预测结果。

X, y = load_data(r"data.csv")
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.25, random_state=0)

# 定义特征列列表
my_feature_columns = []`A

for key in train_X.keys():
    # 创建tensorflow特征列，并加入到特征列表当中。
    my_feature_columns.append(tf.feature_column.numeric_column(key=key))

classifier = tf.estimator.DNNClassifier(feature_columns=my_feature_columns, hidden_units=[512] * 2, n_classes=10, optimizer="SGD")
classifier.train(input_fn=lambda : train_input_fn(train_X, train_y))
classifier.evaluate(input_fn=lambda : eval_input_fn(test_X, test_y))
