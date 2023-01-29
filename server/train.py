"""Run with python train.py"""
import joblib
from rich import print
from rich.panel import Panel
from sklearn import datasets
from sklearn import metrics
from sklearn import svm
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(X_train, y_train)
print(
    Panel(f"Accuracy: [blue]{metrics.accuracy_score(y_test, clf.predict(X_test))}")
)

joblib.dump(clf, 'model.joblib')
