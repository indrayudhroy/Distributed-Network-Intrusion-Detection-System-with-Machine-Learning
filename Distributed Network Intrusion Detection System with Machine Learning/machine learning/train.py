import load
from sklearn import tree
from sklearn.externals.six import StringIO
import sklearn.cross_validation
from sklearn.ensemble import RandomForestClassifier
from  sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
#import time
data, skf = load.load_iscx()

X, y = data.data, data.target


clf = tree.DecisionTreeClassifier(criterion='entropy')
#clf = SVC()


#scores = sklearn.cross_validation.cross_val_score(clf, data.data, data.target, cv=skf)

#print scores

for train_index, test_index in skf:
	clf = clf.fit(X[train_index], y[train_index])
	print	sklearn.metrics.recall_score(y[test_index],clf.predict(X[test_index]))


with open("data.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)
#time.sleep(1)
#exec("dot -Tpng data.dot -o ISCX34.png")

#print data.target_names



# 22,2,2,2,42,2,23,0,2