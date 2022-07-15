from driver import classDriver
import random
fp2=[[98581, 98721, 99537, 99743, -1, 101458, 98275, 97921, 99306, 99490, 99037, 98268, 99360, 97417, 97294, 100703, 98370, 99221, 98556, 99262],[80953, 80816, 82827, 80765, 82233, 86213, 82336, 80088, 81539, 79580, 80901, 80362, 80594, -1, 79838, 80460, 83963, 80905, 79613, 80332],[83923, 90374, 84656, 85520, 84324, 87370, 86779, 83454, 86408, 85063, 84969, 84415, 84706, 83481, 83916, 84977, 83826, 84925, 83359, 87628],[85184, 83849, 84622, 85577, 85168, 88959, 84083, 83345, 84225, 84031, 84634, 84294, 84094, 83809, 83880, 85478, 84227, 84923, 83218, 84780],[76503, -1, 75429, 77760, 77588, 78652, 76203, -1, 76506, 76665, 77812, 76884, 77305, 75056, -1, 77932, 79704, 81832, 79662, 75972],[107828, 107940, 108079, -1, 108378, 109582, 108339, 106942, 107970, 108715, 108175, 107947, 108849, 106915, 107187, 109599, 107399, 109679, 108026, 108888],[100458, 100008, 99413, 99895, 99634, 102056, 99209, 98646, 98557, 98522, 99743, 99241, 98975, 97825, 98506, 101037, 98747, 99524, 97834, 99713],[70646, 70372, 70358, 70767, 73408, 72076, -1, 69911, 70148, 70151, 73877, 70478, 73936, 69724, 69583, 71187, 70126, 70110, 70034, 70723],[70170, 75688, 72420, 70586, 70311, 71694, 70624, 69935, 69665, 73320, 70474, 71433, 74124, 72702, 69651, 70972, 74354, 69901, 69868, 70513],[],[84449, 83959, 84664, 85207, 84256, 87058, 84570, 85079, 84415, 84162, 84255, -1, 84493, 85030, 85132, 86452, 84110, 84972, 84070, 85386],[-1, 110591, 110818, 111776, 109357, -1, 111099, 110282, 110781,107719 , 110724, 111550, 110677, 109776, 110231, 110099, 107131, 111337, 109265, 109387],[76641, 75774, 76599, 77623, 76601, -1, 75979, 75770, 75478, 76223, 76455, 76803, 76010, 75377, -1, 77726, 75995, 76934, 75662, 76457],[],[],[89016, 88827, 89028, 89288, 89419, 89941, 88953, 88721, 89283, 88529, 88928, 90201, 88892, 88325, 90184, 90020, 88771, 89217, 88019, 89496],[102345, 102325, 102277, 103954, 102603, 104957, 103119, 102077, 102200, 102494, 102424, 103345, 102605, 101514, 102678, 105797, 102457, 104007, 102210, 102655],[-1, 82715, 82811, 83775, 82094, 84571, 82001, 81553, 82335, 82248, 82894, 82472, 83019, 81059, 82166, 84730, 82319, -1, 86578, 83493],[],[90081, 89653, 89075, 90526, 90658, -1, 90094, 89650, 89287, 89608, 89913, 91331, 88950, 88378, 90023, 90738, 89487, 89832, 88123, 89778],[95203, -1, 95586, 95887, -1, 96635, -1, 95151, 95436, 94574, 95899, 96187, 94581, 95067, 93992, 96108, 94975, 94874, 94806, 95265],[90182, 90030, 90411, 90947, 89947, 92933, 90469, 89144, 89940, 89933, 90739, 90341, 89983, 88523, 89381, 91903, 90401, 90980, 89425, 90967]]
qualify=[[89927, 89974, 92056, 91936, 91238, 93273, 89809, 90659, 90249, 89678, 90601, 90607, 91724, 88997, 89385, 92449, 90009, 91316, 89586, 90708],[74826, 74718, 75394, 75593, 75974, 76797, 74790, 74446, 75593, 74740, 75138, -1, 75117, 74498, 74411, 76279, 75199, 75261, 74672, 76122],[79839, 78481, 78970, 80285, 79748, 80912, 79052, 78845, 79456, 78769, 79913, 79463, 78586, 78650, 77968, -1, 78813, 79109, 78348, 79216],[77622, 77696, 78079, 79219, 78917, 79807, 77982, 77669, 77966, 77510, 77974, 78556, 77580, 76777, 76741, 79117, 77620, 78445, 76873, 78356],[71598, 70620, 71309, 72366, 71642, 72958, 70900, 71019, 72205, 70346, 71600, 72096, 71486, 70576, 71095, -1, 70611, 71830, 70601, 71409],[102304, 101747, 102224, 103128, 102587, 104238, 101565, 101630, 102195, 101218, -1, 101654, 102273, 101563, 101450, 104158, 101576, 102728, 102106, -1],[91382, 91252, 91767, 93062, 93354, 93554, 90868, 90445, 91340, 90987, -1, -1, 91736, 89990, 90248, 92942, 90840, 92065, 90376, 91813],[64808, 64120, 64875, 65175, 65429, 66192, 64236, 64168, 64574, 64472, 64663, 64514, 65217, 63841, 64067, 66041, 64800, 64671, 64035, 64913],[64719, 63768, 64493, 65195, 65009, 65951, 64107, 63990, 64472, 64600, 64547, 64273, 65051, 63720, 64014, 65427, 64559, 64553, 64049, 64782],[],[76871, 76385, 76750, 78036, 77553, 78922, 76394, 76421, 76541, 76496, 76893, 77919, 76653, 75650, 75419, -1, 76649, 77944, 75734, 77583],[117127, 116025, 116814, 118056, 124452, 124939, 116440, 116886, 118205, 117721, 118231, 122413, 117354, 116559, 116229, 123973, 118137, 116950, 116295, 122306],[69865, 70406, 70731, 70093, 71301, 71875, 69478, 70530, 69956, 69437, 70367, 70462, 69919, 68885, 68923, 71387, 69537, 70332, 69222, 69590],[],[],[85881, 83954, 84795, 86086, 87525, 88449, 83326, 83706, 83477, 83265, 84305, 84054, 84842, 83196, 82868, 85200, 85177, 85007, 82998, 86430],[93808, 93880, 95281, 95995, 96311, 96796, 94118, 93134, 95756, 93606, 95983, 94918, 95377, 92910, 93119, 96499, 93792, 95746, 93475, 95794],[76763, 77473, 77502, 78756, 77606, 79303, 76456, 76342, 78452, 76748, 80873, 76701, 78126, 76225, 76020, 78858, 76761, 77958, 75875, 77897],[],[82597, 81731, 82146, 83213, 83156, 85859, 81640, 82346, 81670, 82463, 82460, 81881, 82012, 81282, 80827, 83407, 81840, 82756, 81478, 83262],[88216, 88180, 89198, 89177, 88856, 90473, 88125, 87946, 88920, 88054, 89368, 88222, 88574, 87653, 87511, 89464, 88237, 88926, 87622, 88616],[83409, 82931, 84225, 84338, 84779, 85685, 83489, 82947, 83460, 83122, 84061, 83220, 83389, 82109, 82480, 84906, 82992, 84423, 83036, 84118]]
tyreFP2=[["M", "M", "M", "M", "M", "S", "S", "M", "M", "S", "M", "M", "S", "M", "M", "H", "M", "S", "M", "H"],["S", "S", "M", "M", "M", "M", "S", "M", "S", "M", "M", "M", "M", "M", "M", "M", "S", "M", "M", "M"],["M", "M", "M", "M", "S", "H", "M", "M", "M", "M", "M", "M", "M", "M", "S", "S", "M", "M", "M", "M"],["S", "M", "M", "M", "M", "S", "S", "S", "S", "M", "M", "S", "M", "S", "M", "S", "S", "S", "M", "S"],["M", "M", "S", "S", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "S", "M", "H", "M", "M", "M"],["M", "S", "H", "M", "M", "H", "M", "S", "S", "M", "S", "S", "M", "S", "M", "H", "M", "M", "M", "S"],["S", "S", "M", "H", "S", "S", "S", "M", "H", "H", "M", "M", "M", "M", "M", "M", "S", "M", "M", "M"],["S", "S", "M", "M", "M", "M", "F", "S", "M", "H", "M", "S", "M", "H", "S", "S", "S", "H", "F", "S"],["S", "S", "H", "M", "M", "S", "M", "M", "S", "M", "S", "S", "S", "M", "M", "S", "H", "M", "M", "M"],[],["M", "S", "S", "M", "S", "H", "S", "M", "S", "M", "M", "S", "M", "M", "M", "S", "M", "S", "S", "S"],["M", "H", "S", "M", "M", "M", "M", "M", "S", "M", "M", "M", "S", "M", "M", "M", "M", "M", "M", "M"],["H", "S", "S", "H", "S", "S", "S", "S", "H", "M", "M", "M", "M", "S", "S", "M", "S", "S", "S", "M"],[],[],["S", "H", "M", "M", "M", "M", "M", "M", "S", "M", "M", "M", "H", "M", "M", "M", "M", "M", "M", "M"],["S", "M", "H", "M", "M", "H", "S", "M", "M", "M", "M", "M", "H", "M", "M", "M", "S", "M", "M", "M"],["H", "M", "M", "M", "M", "M", "M", "M", "H", "M", "M", "M", "M", "M", "S", "S", "M", "M", "H", "S"],[],["S", "S", "M", "H", "H", "S", "H", "S", "M", "S", "S", "S", "S", "S", "S", "S", "H", "M", "M", "M"],["S", "M", "M", "M", "M", "S", "S", "M", "S", "M", "M", "H", "S", "M", "M", "H", "M", "H", "H", "H"],["S", "M", "M", "M", "H", "M", "M", "M", "M", "S", "S", "S", "S", "S", "M", "M", "M", "M", "M", "M"]]
gridPosition=[[6,7,20,17,14,19,5,11,9,4,10,13,16,1,2,18,8,15,3,12],[6,7,13,14,16,19,5,2,15,4,10,20,9,3,1,18,11,12,8,17],[16,7,10,18,15,20,9,4,13,8,17,14,6,3,2,19,5,11,1,12],[7,9,13,19,17,20,12,8,10,4,11,16,5,2,1,18,6,15,3,14],[12,5,8,18,14,19,6,9,17,1,13,16,11,2,7,20,4,15,3,10],[13,9,11,16,14,18,4,6,8,1,19,7,12,3,2,17,5,15,10,20],[10,8,12,16,17,18,6,4,9,7,19,20,11,1,2,15,5,14,3,13],[13,3,14,16,18,20,6,4,9,7,10,8,17,1,2,19,12,11,5,15],[13,2,8,18,16,20,6,3,14,12,10,7,17,1,4,19,11,9,5,15],[],[11,6,10,18,13,19,5,4,9,7,12,16,8,3,1,20,15,17,2,14],[4,14,5,10,20,18,6,7,13,9,19,16,8,1,3,17,11,2,12,15],[10,13,17,14,18,20,4,16,9,5,12,15,8,1,2,19,6,11,3,7],[],[],[20, 7, 10, 15, 17, 18, 4, 6, 5, 3, 8, 9, 12, 2, 11, 14, 19, 13, 1, 1],[6,7,18,14,15,17,8,3,19,4,13,10,11,1,2,16,5,20,9,12],[6,7,18,14,15,17,8,3,19,4,13,10,11,1,2,16,5,20,9,12],[],[14,6,10,17,16,20,4,11,5,13,12,8,9,2,1,19,7,15,3,18],[11,7,17,16,12,20,6,5,13,4,18,8,9,3,1,19,15,14,2,10],[10,3,15,16,18,20,12,4,11,7,13,8,9,1,2,19,5,17,6,14]]
laps=[57,63,66,66,78,51,53,71,71,52,70,44,72,53,53,58,56,71,71,57,50,58]
driverNames=["ricciardo","norris","vettel","latifi","raikkonen","mazepin","gasly","perez","alonso","leclerc","stroll","tsunoda","ocon","max_verstappen","hamilton","mick_schumacher","sainz","russell","bottas","giovinazzi"]
driverNo=[3,4,5,6,7,9,10,11,14,16,18,22,31,33,44,47,55,63,77,99]
driverLapVariabilities=[461, 433, 495, 575, 551, 715, 479, 467, 478, 452, 520, 545, 514, 399, 437, 643, 439, 538, 487, 536]
driverDNF=[1,1,2,3,3,6,3,2,2,2,3,4,3,2,1,3,0,4,4,1]
driverSpin=[0,4,5,6,6,14,3,7,3,6,1,7,1,1,1,3,5,1,2,3]
driverLapCount=[1003,971,972,904,911,639,874,936,982,905,898,823,907,977,1005,788,1029,891,880,969]
def simulate():
    season=list()
    for i1 in range(0,22):
        if len(fp2[i1])==0 or fp2[i1] is None:
            season.append(None)
            continue
        race=list()
        #find the fastest FP2 and qualify
        fastestQualify=min(qualify[i1])
        fastestFP2=min(fp2[i1])    
        for i2 in range(0,20):#initialize driver Parameters
            driver=classDriver(driverNo[i2],driverNames[i2])
            if(fp2[i1][i2]==-1):
                    if i2==0:
                        fp2[i1][i2]=fp2[i1][1]
                    elif i2==1:
                        fp2[i1][i2]=fp2[i1][0]
                    elif i2==2:
                        fp2[i1][i2]=fp2[i1][10]
                    elif i2==3:
                        fp2[i1][i2]=fp2[i1][17]
                    elif i2==4:
                        fp2[i1][i2]=fp2[i1][19]
                    elif i2==5:
                        fp2[i1][i2]=fp2[i1][15]
                    elif i2==6:
                        fp2[i1][i2]=fp2[i1][11]
                    elif i2==7:
                        fp2[i1][i2]=fp2[i1][13]
                    elif i2==8:
                        fp2[i1][i2]=fp2[i1][12]
                    elif i2==9:
                        fp2[i1][i2]=fp2[i1][16]
                    elif i2==10:
                        fp2[i1][i2]=fp2[i1][2]
                    elif i2==11:
                        fp2[i1][i2]=fp2[i1][6]
                    elif i2==12:
                        fp2[i1][i2]=fp2[i1][8]
                    elif i2==13:
                        fp2[i1][i2]=fp2[i1][7]
                    elif i2==14:
                        fp2[i1][i2]==fp2[i1][18]
                    elif i2==15:
                        fp2[i1][i2]=fp2[i1][5]
                    elif i2==16:
                        fp2[i1][i2]=fp2[i1][9]
                    elif i2==17:
                        fp2[i1][i2]=fp2[i1][3]
                    elif i2==18:
                        fp2[i1][i2]=fp2[i1][14]
                    elif i2==19:
                        fp2[i1][i2]=fp2[i1][4]
            if(qualify[i1][i2]==-1):
                    if i2==0:
                        qualify[i1][i2]=qualify[i1][1]
                    elif i2==1:
                        qualify[i1][i2]=qualify[i1][0]
                    elif i2==2:
                        qualify[i1][i2]=qualify[i1][10]
                    elif i2==3:
                        qualify[i1][i2]=qualify[i1][17]
                    elif i2==4:
                        qualify[i1][i2]=qualify[i1][19]
                    elif i2==5:
                        qualify[i1][i2]=qualify[i1][15]
                    elif i2==6:
                        qualify[i1][i2]=qualify[i1][11]
                    elif i2==7:
                        qualify[i1][i2]=qualify[i1][13]
                    elif i2==8:
                        qualify[i1][i2]=qualify[i1][12]
                    elif i2==9:
                        qualify[i1][i2]=qualify[i1][16]
                    elif i2==10:
                        qualify[i1][i2]=qualify[i1][2]
                    elif i2==11:
                        qualify[i1][i2]=qualify[i1][6]
                    elif i2==12:
                        qualify[i1][i2]=qualify[i1][8]
                    elif i2==13:
                        qualify[i1][i2]=qualify[i1][7]
                    elif i2==14:
                        qualify[i1][i2]==qualify[i1][18]
                    elif i2==15:
                        qualify[i1][i2]=qualify[i1][5]
                    elif i2==16:
                        qualify[i1][i2]=qualify[i1][9]
                    elif i2==17:
                        qualify[i1][i2]=qualify[i1][3]
                    elif i2==18:
                        qualify[i1][i2]=qualify[i1][14]
                    elif i2==19:
                        qualify[i1][i2]=qualify[i1][4]
            driver.FP2=fp2[i1][i2]
            driver.qualify=qualify[i1][i2]
            driver.gridPosition=gridPosition[i1][i2]
            driver.position=gridPosition[i1][i2]
            driver.DNF=driverDNF[i2]
            driver.spin=driverDNF[i2]
            driver.lapCount=driverLapCount[i2]
            driver.lapTimeVariability=driverLapVariabilities[i2]
            driver.allTime=800*(driver.gridPosition-1)
            driver.timeDifferencePreviousCar=800*(driver.gridPosition-1)
            driver.deltaFP2=driver.FP2-fastestFP2
            driver.deltaQualify=driver.qualify-fastestQualify
            driver.forecastedPrimeTime=driver.FP2+0.5*(driver.deltaQualify-driver.deltaFP2)
            race.append(driver)
        dnfList=list()
        dnfCounter=0
        race.sort(key=lambda x:x.position)
       
        dnfLapNo=3000
        safetyCar=False
        crash=False
        for i2 in range(0,laps[i1]):
            j=0
            for driver in list(race):#adding Lap
                if dnfLapNo+6==i2:
                    safetyCar=False
                if i2==2 or dnfLapNo+9==i2:
                    driver.DRSRule=True
                driver.checkDNF()
                if driver.boolCheckDNF:#DNF OLMA KONTROL
                    driver.position=20-dnfCounter
                    temp=driver
                    race.pop(race.index(driver))
                    dnfList.insert(0,temp)
                    dnfLapNo=i2
                    dnfCounter+=1
                    crash=True
                    continue
                driver.newLap=driver.createRaceLap()
                if safetyCar==True:###SAFETY CAR SİMÜLASYON
                    driver.DRSRule=False
                    if driver.position==1 or driver.timeDifferencePreviousCar<500:
                        driver.newLap*=140/100
                    else:
                        driver.newLap*=120/100
                    if driver.position!=1 and driver.allTime+driver.newLap-400<race[race.index(driver)-1].allTime+race[race.index(driver)-1].newLap:
                        rnd=random.randint(400,500)
                        driver.newLap=race[race.index(driver)-1].allTime+race[race.index(driver)-1].newLap+rnd-driver.allTime
                    continue
                driver.checkOvertaking()
                if driver.DRSSituation==True: #DRS Bonus
                    driver.newLap-=400
                #overtaking model

                if driver.position!=1:
                    prevNewAllTime=race[race.index(driver)-1].allTime+race[race.index(driver)-1].newLap
                    newAllTime=driver.allTime+driver.newLap
                    timeDifferencePreviousCar=newAllTime-prevNewAllTime
                    if timeDifferencePreviousCar<200 and timeDifferencePreviousCar>-1200:
                        rnd=random.randint(200,501)
                        newAllTime=prevNewAllTime+rnd
                        driver.newLap=newAllTime-driver.allTime
                    elif timeDifferencePreviousCar<-1200 and driver.position>2:
                        prev2NewAllTime=race[race.index(driver)-2].allTime+race[race.index(driver)-2].newLap
                        newAllTime=driver.allTime+driver.newLap
                        timeDifference2PreviousCar=newAllTime-prev2NewAllTime
                        if timeDifference2PreviousCar<200 and timeDifference2PreviousCar>-1200:
                            rnd=random.randint(200,301)
                            newAllTime=prev2NewAllTime+rnd
                            driver.newLap=newAllTime-driver.allTime
                            
                        
                if crash==True:
                    safetyCar=True
                    crash=False            

                j+=1
            for driver in race:#adding lap times
                driverLapTimes=list()
                for lap in driver.raceLapTime:#creating list lap
                    driverLapTimes.append(lap)
                driverLapTimes.append(driver.newLap)
                driver.raceLapTime=driverLapTimes
                driver.allTime+=driver.raceLapTime[-1]
            race.sort(key=lambda x:x.allTime)
            race[0].timeDifferencePreviousCar=0
            for j in range(len(race)):
                newList=list()
                for position in race[j].positionList:
                    newList.append(position)
                newList.append(j+1)
                race[j].positionList=newList
                race[j].position=j+1
                if j!=0:
                    race[j].timeDifferencePreviousCar=race[j].allTime-race[j-1].allTime
        race=race+dnfList

        season.append(race)
        print(i1)
        for result in race:
            
            millisecond=result.allTime%1000
            second=result.allTime-millisecond
            second=second/1000
            minute=second
            second=second%60
            minute=minute-second
            minute=minute/60
            if len(result.raceLapTime)==0:
                result.raceLapTime=[0]
            print(str(result.position)+"-) "+result.driverName+"\t"+str(int(minute))+":"+str(int(second))+"."+str(int(millisecond))+"\t"+str(int(result.allTime/len(result.raceLapTime)))+"\t"+str(result.boolCheckDNF)+"\t"+str(result.spinCounter))
        print("*****************************\n")

    return season