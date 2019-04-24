from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

iris = load_iris()
features = iris.data
labels = iris.target

train_feature, test_feature, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=0)

clf = DecisionTreeClassifier(criterion='gini')

clf = clf.fit(train_feature, train_labels)

test_predict = clf.predict(test_feature)

score = accuracy_score(test_labels, test_predict)
print("准确率： %.4lf" % score)
