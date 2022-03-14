class classDriver:
    def __init__(self, driverNo,driverName):
        self.driverNo=driverNo
        self.driverName = driverName
    def addPitLaps(self,pitLaps):
        self.pitLaps=pitLaps
    def addLaps(self,lapTimes):
        self.lapTimes=lapTimes
        self.lastLapNo=len(lapTimes)#Turlar sıfırdan başlıyor gözükür
    def showLapTime(self,lapNo):
        return self.lapTimes[lapNo]
    def showAllLapTimes(self):
        return self.lapTimes
    def showPitLaps(self):
        return self.pitLaps
    def showCountOfLaps(self):
        return self.lastLapNo