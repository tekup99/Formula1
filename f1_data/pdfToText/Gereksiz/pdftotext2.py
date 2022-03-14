import PyPDF2
from PyPDF2.pdf import PageObject

from driver import driver
from textMethods import (defDeleteDriverNamesAndNumbers, defFindDriverNo,
                         defFindNameOfDriver, defPitLap, defPitLapIndex,
                         defReplace, defSplit, deleteF1Writing)

pdfFileObject = open(r"C:\f1_data\pdf\01_brn_practice_1_laptimes.pdf", 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
 
print(" No. Of Pages :", pdfReader.numPages)
#allPagesText=[]
#for i in range(0,pdfReader.numPages):
#    pageObject = pdfReader.getPage(i)
#    allPagesText.append(pageObject.extractText())
pageObject = pdfReader.getPage(0)
a=defSplit("NO\nTIME",pageObject.extractText())#split notime

b=defReplace(a,"\n"," ")# save from \n
driverNames=defFindNameOfDriver(b,"           ")
driverNumbers=defFindDriverNo(b,"           ")
driverDeneme=[]

c=deleteF1Writing(b,"The")#save from the official f1...
d=defDeleteDriverNamesAndNumbers(c,"           ")
merged=[]
for i in range(0,len(d)-1,2):
    merged.append(d[i+1]+d[i])


pitLapIndex=[]
for i in range(0,len(merged)):
    pitLapIndex.append(defPitLapIndex(merged[i]," P "))

pitLap=defPitLap(merged,pitLapIndex)#TODO
for i in range(0,len(driverNames)-1):#insert driverNo and driverNames
    driverDeneme.append(driver(int(driverNumbers[i]),driverNames[i]))
    driverDeneme[i].addPitLaps(pitLap[i])
mergedWithoutP=[]
for row in merged: 
    mergedWithoutP.append(row.replace(" P ", "   "))

pdfFileObject.close()
