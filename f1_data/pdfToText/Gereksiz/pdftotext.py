import PyPDF2
import re
import numpy as np

pdfFileObject = open(r"C:\f1_data\pdf\01_brn_practice_1_laptimes.pdf", 'rb')
 
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
 
print(" No. Of Pages :", pdfReader.numPages)
merge=[10000000]
for pageNumber in range(0, pdfReader.numPages-1):#DEĞİŞTİR!!!!!

    pageObject = pdfReader.getPage(pageNumber)
    a=re.split("NO\nTIME",pageObject.extractText())#NO TIMELAR AYRILIR
    b=[]]
    for a1 in a:
        b.append(a1.replace("\n", "  ").replace("           ", " "))#Pilot İsimleri Öncesi 3 Boşluk Verilir ve \nler kaldırılır
    p=" P "
    s=[]
    for b1 in b:
        s.append([q+p for q in b1.split(p) if q]) #Plerden kurtulma
    s=[x for sublist in s for x in sublist] #1D Dönüştürme
    c=[]
    for i in range(0,len(s)-1):
        c.append(s[i].split("   "))#Pilot İsimleri Ayrıştırılmaya çalışılır. 2D oluşur

    d = [x for sublist in c for x in sublist]#1D'ye dönüştürülür
    e=[]
    for d1 in d:
        e.append(d1.replace("  ", " "))
    merge=e+merge
print(merge)
pdfFileObject.close()