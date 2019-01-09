import csv
import re
from datetime import datetime as dt
i = 0
path = "C:\\Users\\student\\Project\\sniffer\\"
file = "mypcap1.pcap"
csvfile = "C:\\Users\\student\\Project\\sniffer\\captureCSV.csv"
fcsv = open(csvfile, "ab")
fw = csv.writer(fcsv)
UID = 0
with open(path+file, "r") as fptr:
    linetmp = ""
    lines = []
    for line in fptr:
        tokens = []
        line = line.strip()
        linetmp += " " + line
        i += 1
        if i == 2:
            lines.append(linetmp.strip())
            i = 0
            linetmp = ""
    transactionStart = 0
    transaction = []
    tmptrans = []
    for item in lines:
        if "(correct)" in item and transactionStart != 1:
            transactionStart = 1
            tmptrans.append(item)
            continue
        if "(correct)" in item and transactionStart == 1:
            tmptrans.append(item)
            transaction.append(tmptrans)
            tmptrans = []
            transactionStart = 0
    toCSV = []
    for trans in transaction:
        startTime = ""
        timeFlag = 0
        stopTime = ""
        source = ""
        destination = ""
        for item in trans:
            tmpIP = []
            IP = []
            UID += 1
            toCSV.append(UID)
            toCSV.append("SSH")
            matchTime = re.search(r"^\d+:\d+:\d+\.\d+\s", item)
            toCSV.append(matchTime.group().strip())
            if timeFlag == 0:
                startTime = matchTime.group().strip()
                startTime = dt.strptime(startTime, "%H:%M:%S.%f")
                timeFlag = 1
            else:
                stopTime = matchTime.group().strip()
                stopTime = dt.strptime(stopTime, "%H:%M:%S.%f")
                duration = (stopTime - startTime).seconds
                timeFlag = 0
            matchIP = re.search(r"\s\d+\.\d+\.\d+\.\d+\.\d+\s>\s\d+\.\d+\.\d+\.\d+\.\d+", item)
            tmpIP = matchIP.group().split(">")
            for i in tmpIP:
                IP.append(i.strip())
            source = IP[0]
            toCSV.append(source)
            destination = IP[1]
            toCSV.append(destination)
            matchSizeString = re.search(r"length\s\d+\)", item)
            matchSize = re.search(r"\d+", matchSizeString.group())
            matchProtoString = re.search(r"\sproto\s[A-Za-z0-9]+\s", item)
            protoList = matchProtoString.group().split()
            protocol = protoList[1].strip()
            toCSV.append(protocol)
            toCSV.append("L2L")
            fw.writerow(toCSV)
            toCSV = []
fcsv.close()
