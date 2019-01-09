import storm
import pickle
from sklearn.externals import joblib

class DDosBolt(storm.BasicBolt):
    def process(self,tup):
		clf = joblib.load('/home/student/storm/apache-storm-0.10.0/project/code/DDosTrain.pkl')
        predict = clf.predict(tup[1:-1])
		output_tuple = tup[0] + predict
		storm.emit([output_tuple])
	DDosBolt.run()
