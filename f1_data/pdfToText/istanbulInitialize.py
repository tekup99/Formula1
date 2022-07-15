from raceSimulator import convertStringToMilliseconds
from driver import classDriver
def defIstanbulInitialize(FP2AverageList:list()):
    driverNames=["ricciardo","norris","vettel","latifi","raikkonen","mazepin","gasly","perez","alonso","leclerc","stroll","tsunoda","ocon","max_verstappen","hamilton","mick_schumacher","sainz","russell","bottas","giovinazzi"]
    driverNo=[3,4,5,6,7,9,10,11,14,16,18,22,31,33,44,47,55,63,77,99]
    driverLapVariabilities=[461, 433, 495, 575, 551, 715, 479, 467, 478, 452, 520, 545, 514, 399, 437, 643, 439, 538, 487, 536]
    driverDNF=[1,1,2,3,3,6,3,2,2,2,3,4,3,2,1,3,0,4,4,1]
    driverSpin=[0,4,5,6,6,14,3,7,3,6,1,7,1,1,1,3,5,1,2,3]
    driverLapCount=[1003,971,972,904,911,639,874,936,982,905,898,823,907,977,1005,788,1029,891,880,969]
    FP2Istanbul=[89017,88827,89029,89289,89420,89941,88954,88721,89284,88529,88928,90202,88892,88325,87878,90021,88771,89218,88020,89497]
    FP2IstanbulTyre=["S", "H", "M", "M", "M", "M", "M", "M", "S", "M", "M", "M", "H", "M", "M", "M", "M", "M", "M", "M" ]
    bestFP2Istanbul=min(FP2Istanbul)
    quaIstanbul=['1:25.881','1:23.954','1:24.795','1:26.086','1:27.525','1:28.449','1:23.326','1:23.706','1:23.477','1:23.265','1:24.305','1:24.054','1:24.842','1:23.196','1:22.868','1:25.200','1:25.177','1:25.007','1:22.998','1:26.430']
    gridIstanbul=[20, 7, 10, 15, 17, 18, 4, 6, 5, 3, 8, 9, 12, 2, 11, 14, 19, 13, 1, 16]
    quaIstanbulAsInt=list()
    for lap in quaIstanbul:
        quaIstanbulAsInt.append(convertStringToMilliseconds(lap))
    bestQuaIstanbul=min(quaIstanbulAsInt)
    driverParametersList=list()
    for i in range(0,len(driverNames)):
        driverParameters=classDriver(driverNo[i],driverNames[i])
        driverParameters.lapCount=driverLapCount[i]
        driverParameters.DNF=driverDNF[i]
        driverParameters.spin=driverSpin[i]
        driverParameters.qualifyingResult=quaIstanbulAsInt[i]
        driverParameters.FP2Istanbul=FP2Istanbul[i]
        driverParameters.FP2Delta=FP2Istanbul[i]-bestFP2Istanbul
        driverParameters.qualifyingDelta=quaIstanbulAsInt[i]-bestQuaIstanbul
        driverParameters.forecastedPrimeTime=FP2Istanbul[i]+ 0.5*(driverParameters.qualifyingDelta-driverParameters.FP2Delta)
        driverParameters.lapTimeVariability=driverLapVariabilities[i]
        driverParameters.FP2Tyre=FP2IstanbulTyre[i]
        driverParameters.position=gridIstanbul[i]
        driverParameters.grid=gridIstanbul[i]
        if driverParameters.FP2Tyre=="S":
            driverParameters.forecastedPrimeTime+=900
        elif driverParameters.FP2Tyre=="M":
            driverParameters.forecastedPrimeTime+=400
        driverParameters.forecastedPrimeTime+=6300
        driverParametersList.append(driverParameters)
    return driverParametersList

def defIstanbulPaceFP2(practiceResults:list):
    season=list()
    for practice in practiceResults:
        turkishLaps=list()
        if practiceResults.index(practice)==9 or practiceResults.index(practice)==13 or practiceResults.index(practice)==14 or practiceResults.index(practice)==18:
            season.append(None)
            continue
        for driver in practice[1]:
            lapsSuitable=list()
            j=999
            for i in range(1,len(driver.lapTimes)):
                if convertStringToMilliseconds(driver.lapTimes[i])<112000 and convertStringToMilliseconds(driver.lapTimes[i-1])<112000 and convertStringToMilliseconds(driver.lapTimes[i])-convertStringToMilliseconds(driver.lapTimes[i-1])<2000 and convertStringToMilliseconds(driver.lapTimes[i])-convertStringToMilliseconds(driver.lapTimes[i-1])>-2000:
                    if i!=j:
                        lapsSuitable.append(convertStringToMilliseconds(driver.lapTimes[i-1]))
                    lapsSuitable.append(convertStringToMilliseconds(driver.lapTimes[i]))
                    j=i+1
            if len(lapsSuitable)==0:
                turkishLaps.append(None)
            else:
                turkishLaps.append(sum(lapsSuitable)/len(lapsSuitable))
        season.append(turkishLaps)
    for week in season:
        if week==None:
            print("*******************None******************")
            continue
        for driver in week:
            if driver==None:
                print("-1")
            else:
                print(int(driver))
        print("**********************")
    return season