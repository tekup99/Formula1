from ast import List
from driver import classDriver
from numpy import double

def raceSimulator(drivers:list,lastLapNo:int):
    startRaceSimulator()
    avarageOfFP2(drivers)
    fastestFP2=fastestDriverOfFP2(drivers)
    DEFdeltaFP2(drivers,fastestFP2)
    fastestQualifying=fastestQualifying(drivers)
    DEFdeltaQualifying(drivers,fastestQualifying)
    for i in range(lastLapNo):
        updateTotalTime(drivers,i)


def startRaceSimulator(drivers:list):
    for driver in drivers:
        driver.totalTime=0.25*(driver.driverRank-1)

def updateTotalTime(drivers:list,i:int):
    for driver in drivers:
        driver.totalTime+=convertStringToMilliseconds(driver.lapTimes[i])
    drivers(checkRanks)


def checkRanks(drivers:list):
    temp=classDriver()
    for i in range(drivers.length()-1):
        for j in range(i,drivers.length()-1):
            if(drivers[i].totalTime<drivers[j].totalTime):
                temp=drivers[i]
                drivers[i]=drivers[j]
                drivers[j]=temp

def avarageOfFP2(drivers:list):
    for driver in drivers:
        avg=sum(drivers.lapTimes)/len(drivers.lapTimes)
        forecast=0
        countLap=0
        for laptime in driver.lapTimes:
            if(laptime-avg<10):#second
                forecast=+laptime
                countLap+=1
        driver.avarageOfFP2=forecast/countLap
    
def fastestDriverOfFP2(drivers:list):
    temp=9999999999999
    for driver in drivers:
        if(temp<driver.averageOfFP2):
            temp=driver.averageOfFP2
    return temp
    
def DEFdeltaFP2(drivers:list,fastestDriverOfFP2:int):
    for driver in drivers:
        driver.deltaFP2=fastestDriverOfFP2-driver.averageOfFP2
def fastestDriverOfQualifying(drivers:list):
    temp=9999999999999
    for driver in drivers:
        if(temp<driver.qualifying):
            temp=driver.qualifying
    return temp

def DEFdeltaQualifying(drivers:list,fastestDriverOfQualifying:int):
    for driver in drivers:
        driver.deltaQualifying=fastestDriverOfQualifying-driver.averageOfQualifying

def convertStringToMilliseconds(lapTime:str):
    if lapTime[6]==':' or lapTime[5]==':':
        return 999999
    doubledat=lapTime.find(":")
    dat=lapTime.find(".")   
    millisecond=int(lapTime[0:doubledat])*60000+ int(lapTime[doubledat+1:dat])*1000 + int (lapTime[dat+1:len(lapTime)]) 
    return millisecond