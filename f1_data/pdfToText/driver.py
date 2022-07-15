from driverParameters import driverParameters
import random
class classDriver:
    
    startBonusPenalty=float
    lapTimeVariability=int
    boolCheckDNF=False
    DNF=int
    spin=int
    spinCounter=0
    tyreDegradation=float
    positionList=list()
    position=int
    lapCount=int
    allTime=0
    raceLapTime=list()
    timeDifferenceNextCar=float
    timeDifferenceFirstCar=float
    timeDifferencePreviousCar=float
    DRSSituation=False
    DRSRule=False
    def __init__(self, driverNo,driverName):
        self.driverNo=driverNo
        self.driverName = driverName
    def createRaceLap(self):
        rnd=random.randint(0,self.lapTimeVariability+1)
        firstLapIndex=800
        lostSpin=self.checkSpin()
        lapTime=self.forecastedPrimeTime+rnd+lostSpin
        if len(self.raceLapTime)==0:
            return self.position*firstLapIndex+lapTime
        if self.DRSSituation==True:
            return lapTime-400
        return lapTime
    def checkDNF(self):
        lapCounter=self.lapCount
        DNF=self.DNF
        if DNF==0:
            lapCounter*=2
            DNF=1
        rnd=random.randint(0,lapCounter)
        if rnd<DNF:#if dnf happen
            self.boolCheckDNF=True
    def checkSpin(self):
        lapCounter=self.lapCount
        spin=self.spin
        if spin==0:
            lapCounter*=2
            spin=1
        rnd=random.randint(0,lapCounter*3)
        if rnd<spin:
            self.spinCounter+=1
            rnd2=random.randint(2000,16000)
            return rnd2
        return 0
    def checkOvertaking(self):
        if self.DRSRule==True and self.timeDifferencePreviousCar<=1000 and self.position!=1:
            self.DRSSituation=True
        else:
            self.DRSSituation=False
    def addPitLaps(self,pitLaps):
        self.pitLaps=pitLaps
    def addLaps(self,lapTimes):
        self.lapTimes=lapTimes
    #    self.lastLapNo=len(lapTimes)#Turlar sıfırdan başlıyor gözükür
    def showLapTime(self,lapNo):
        return self.lapTimes[lapNo]
    def showAllLapTimes(self):
        return self.lapTimes
    def showPitLaps(self):
        return self.pitLaps
    def showCountOfLaps(self):
        return self.lastLapNo