import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.model_selection import cross_val_score

train_data = pd.read_csv('./train.csv')
test_data = pd.read_csv('./test.csv')

# 数据清洗
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S', inplace=True)

# 特征选择
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]
dvec = DictVectorizer(sparse=False)

# print(train_features)
train_features = dvec.fit_transform(train_features.to_dict(orient="record"))
print(dvec.feature_names_)

clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(train_features, train_labels)

train_features = dvec.transform(train_features.to_dict(orient="record"))
pred_lables = clf.predict(test_features)

# 得到决策树准确率
acc_decision_tree = round(clf.score(train_features, train_labels), 6)
print(u'score 准确率为 %.4lf' % acc_decision_tree)

# K折交叉验证
print(u'cross_val_score 准确率为 %.4lf' % np.mean(cross_val_score(clf, train_features, train_labels, cv=10)))




# print(train_data['Embarked'].value_counts())
# print(train_data.info())
# print('-'*30)
# print(train_data.describe())
# print('-'*30)
# print(train_data.describe(include=['O']))
# print('-'*30)
# print(train_data.head())
# print('-'*30)
# print(train_data.tail())

