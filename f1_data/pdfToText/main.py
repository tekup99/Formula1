import time
from getTyre import getTyre
from tyreLinks import getLinks
from practicePaths import getPracticePaths
from pdftotext import practiceResult
from raceSimulator import raceSimulator
from qualifyingAndRace import getQualifying
from qualifyingAndRace import getRaceResults
from raceSimulator import convertStringToMilliseconds
from qualifyingAndRace import lapTimeVariability
from istanbulInitialize import defIstanbulInitialize
from istanbulInitialize import defIstanbulPaceFP2
from driver import classDriver
from raceSimulate import simulate
import statistics
import math
import random
result=simulate()
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

avgFP2=defIstanbulPaceFP2(practiceResults)

qualityResults=getQualifying()
for qualify in qualityResults:
    qualify.sort(key=lambda x:x.driverNo)
    if len(qualify)!=20:
        print("")
temp=qualityResults[12][18]
qualityResults[12].pop(18)
qualityResults[12].insert(4,temp)
temp=qualityResults[2][15]
temp.lapTimes=None
qualityResults[4].insert(15,temp)
for saturday in qualityResults:
    for driver in saturday: 
        if driver.lapTimes is None or len(driver.lapTimes)==0:
            print("-1")
        else:
            driver.lapTimes.sort()
            print(driver.lapTimes[0])
    print("**********************************")

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
avgFP2=defIstanbulPaceFP2(practiceResults)

        
driverParameters =defIstanbulInitialize()

simulate(driverParameters)
raceResults=getRaceResults()
driverVariability=lapTimeVariability(raceResults)





start = time.time()
tyreLinks=getLinks()
tyreResults= []

for link in tyreLinks:
    tyreResults.append(getTyre(link))






stop = time.time()
print("The time of the run:", stop - start)
print("a")