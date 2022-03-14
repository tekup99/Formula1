import PyPDF2
from PyPDF2.pdf import PageObject
import datetime

from driver import classDriver
from textMethods import (defDeleteDriverNamesAndNumbers, defFindDriverNo,
                         defFindNameOfDriver, defPitLap, defPitLapIndex,
                         defReplace, defSplit, deleteF1Writing,defFindLapNo,defFindLapTimes)
def practiceResult(path):
    pdfFileObject = open(path, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

    print(" No. Of Pages :", pdfReader.numPages)
    allPagesText=[]
    for i in range(0,pdfReader.numPages):
        pageObject = pdfReader.getPage(i)
        allPagesText.append(pageObject.extractText())
    driverNames=[]
    driverNumbers=[]
    driverDeneme=[]
    merged=[]
    pitLap=[]
    for page in allPagesText:
        a=defSplit("NO\nTIME",page)#split notime

        b=defReplace(a,"\n"," ")# save from \n
        driverNames+=defFindNameOfDriver(b,"           ")
        driverNumbers+=defFindDriverNo(b,"           ")
        c=deleteF1Writing(b,"The")#save from the official f1...
        d=defDeleteDriverNamesAndNumbers(c,"           ")
    
        for i in range(0,len(d)-1,2):
            merged.append(d[i+1]+d[i])
        pitLapIndex=[]
        for i in range(0,len(merged)):
            pitLapIndex.append(defPitLapIndex(merged[i]," P "))

    pitLap+=defPitLap(merged,pitLapIndex)
    for i in range(0,len(driverNames)):#insert driverNo and driverNames
        driverDeneme.append(classDriver(int(driverNumbers[i]),driverNames[i]))
        driverDeneme[i].addPitLaps(pitLap[i])
    mergedWithoutP=[]
    for row in merged: 
        mergedWithoutP.append(row.replace(" P ", "   "))
    indexesLapNoAndTime=[]
    for row in mergedWithoutP:#Find "   " indexes
        indexesLapNoAndTime.append(defPitLapIndex(row,"   "))
    lapTimes=defFindLapTimes(mergedWithoutP,indexesLapNoAndTime)
    for i in range(0,len(driverDeneme)):
        driverDeneme[i].addLaps(lapTimes[i])
    pdfFileObject.close()
    return driverDeneme
