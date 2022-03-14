import re
import numpy as np
def defSplit(string,text):
    return re.split(string,text)
def defReplace(list,exchanged,changer):
    result=[]
    for row in list:
        result.append(row.replace(exchanged,changer))
    return result
def defFindNameOfDriver(text,searched):
    name=[]
    for string in text:
        start=string.find(searched)
        end=len(string)
        if start!=-1:
            name.append(string[start:end-1].replace("           ", ""))
    return name
def defFindDriverNo(text,searched):
    number=[]
    for string in text:
        string=" "+string
        end=string.find(searched)
        if end!=-1:
            number.append(string[end-2:end].replace(" ", ""))
    return number
def deleteF1Writing(text,searched):
    result=[]
    for string in text:
        if string.find(searched)==-1:
            result.append(string)
        else:
            result.append(string[0:string.find(searched)])
    return result
def defDeleteDriverNamesAndNumbers(text,searched):
    result=[]
    i=-1
    for string in text:
        i+=1
        if i==0:
            continue
        indexOfSpace=string.find("           ")
        if indexOfSpace==-1:
            result.append(string)
        else:
            result.append(string[0:indexOfSpace-2])
    return result
def defPitLapIndex(string, searched):
    return   [ (i.start()) for i in re.finditer(searched, string) ]

def defPitLap(text,indexes):
    result=[]
    i=0
    for string in text:
        driverPitTime=[]
        for j in range(0,len(indexes[i])):
            driverPitTime.append(int(string[indexes[i][j]-2:indexes[i][j]].replace(" ","")))
        result.append(driverPitTime)
        i+=1
    return result
def defFindLapNo(text,indexes):
    result = []
    i=0
    for string in text:
        lapNo=[]
        if string=="    ":
            return None
        if string==" 1   12:22:04        " or string==" 1   14:00:58        ":
            lapNo.append(1)
        else:
            for j in range(0,len(indexes[i])):
                lapNo.append(int(string[indexes[i][j]-2:indexes[i][j]].replace(" ","")))
        result.append(lapNo)
        i+=1
    return result

def defFindLapTimes(text,indexes):
    result=[]
    i=0
    for string in text:
        lapTimes=[]
        for j in range(0,len(indexes[i])):
            tempLapTime=(string[indexes[i][j]+2:indexes[i][j]+11].replace(" ",""))
            if re.search(r'\d\d\d$',tempLapTime)== None:
                tempLapTime=tempLapTime+"0"
            lapTimes.append(tempLapTime)
        result.append(lapTimes)
        i+=1
    return result


