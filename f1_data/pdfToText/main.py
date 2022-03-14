from getTyre import getTyre
from tyreLinks import getLinks
from practicePaths import getPracticePaths
from pdftotext import practiceResult
tyreLinks=getLinks()
tyreResults= []

for link in tyreLinks:
    tyreResults.append(getTyre(link))
practicePaths=getPracticePaths()
practiceResults= []
for mapPracticePath in practicePaths:
    mapPracticeResults=[]
    for practicePath in mapPracticePath:
        if practicePath==None:
            mapPracticeResults.append(None)
        else:
            mapPracticeResults.append(practiceResult(practicePath))
    practiceResults.append(mapPracticeResults)
print("a")