from sklearn.metrics import precision_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

f_Dos = open("/home/student/Dosagg_sorted.txt")
f_DDos = open("/home/student/DDosagg_sorted.txt")
f_Infiltrate = open("/home/student/Infiltrateagg_sorted.txt")
f_BruteForceSSH = open("/home/student/BruteForceagg_sorted.txt")
f_testData = open("/home/student/storm/apache-storm-0.10.0/examples/storm-starter/src/jvm/storm/starter/test-data/MasterTest.csv")

predList = []
testList = []
for i in range(0,166766):
	dos_line = f_Dos.readline()
	ddos_line = f_DDos.readline()
	infil_line = f_Infiltrate.readline()
	brute_line = f_BruteForceSSH.readline()
	testData_line = f_testData.readline()
	pred_dos = int(dos_line.split(",")[9])
	pred_ddos = int(ddos_line.split(",")[9])
	pred_infil = int(infil_line.split(",")[9])
	pred_brute = int(brute_line.split(",")[9])
	pred = pred_dos | pred_ddos | pred_brute | pred_infil
	pred_test = int(testData_line.split(",")[9])
	if pred_test == 1:
		pred_test = 0
	else:
		pred_test = 1
	predList.append(pred)
	testList.append(pred_test)
precscore = precision_score(testList, predList)
print "Precision score %f" % (precscore * 100)

print "----Classification Report----"
report = classification_report(testList, predList)


print report

print "------Confusion matrix------"

cf = confusion_matrix(testList, predList)

print cf
