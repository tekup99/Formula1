from driver import classDriver
from bs4 import BeautifulSoup
import requests
import re
import json
from raceSimulator import convertStringToMilliseconds
import statistics
import math
def getQualifying():
    url="https://ergast.com/api/f1/2021/{0}/qualifying"
    season=list()
    for i in range(1,23):
        formatted_url=url.format(i)
        html_content = requests.get(formatted_url).text
        name_content=re.split("<FamilyName>",html_content)
        name_list=list()
        for name in name_content[1:]:
            nameIndex=name.find("<")
            name_list.append(name[0:nameIndex])
        number_content=re.split("<PermanentNumber>",html_content)
        number_list=list()
        for number in number_content[1:]:
            numberIndex=number.find("<")
            number_list.append(int(number[0:numberIndex]))
        q1_content=re.split("<Q1>",html_content)
        q1_list=list()
        for q1 in q1_content[1:]:
            q1Index=q1.find("<")
            q1_list.append(q1[0:q1Index])
        q2_content=re.split("<Q2>",html_content)
        q2_list=list()
        for q2 in q2_content[1:]:
            q2Index=q2.find("<")
            q2_list.append(q2[0:q2Index])
        q3_content=re.split("<Q3>",html_content)
        q3_list=list()
        for q3 in q3_content[1:]:
            q3Index=q3.find("<")
            q3_list.append(q3[0:q3Index])
        position_content=re.split("position=\"",html_content)
        position_list=list()
        for position in position_content[1:]:
            positionIndex=position.find("\"")
            position_list.append(int(position[0:positionIndex]))
        race=list()
        for j in range(0, len(number_list)):
            driver=classDriver(number_list[j],name_list[j])
            driver.position=position_list[j]
            q_list=list()
            if j<len(q1_list):
                q_list.append(convertStringToMilliseconds(q1_list[j]))
            if driver.position<=len(q2_list):
                q_list.append(convertStringToMilliseconds(q2_list[j]))
            if driver.position<=len(q3_list):
                q_list.append(convertStringToMilliseconds(q3_list[j]))
            if len(q_list)==0:
                driver.addLaps(None)
            driver.addLaps(q_list)
            race.append(driver)
        season.append(race)
    return season

def getRaceResults():
    
    
    url="http://ergast.com/api/f1/2021/{0}/laps/{1}"
    name_list_season=list()
    lapNo_list_season=list()
    lap_list_season=list()
    for i in range(1,23):
        name_list_each_race=list()
        lapNo_list_each_race=list()
        lap_list_each_race=list()
        for j in range(1,100):
            formatted_url=url.format(i,j)
            html_content = requests.get(formatted_url).text
            name_content=re.split("driverId=\"",html_content)
            name_list_each_lap=list()
            for name in name_content[1:]:
                nameIndex=name.find("\"")
                name_list_each_lap.append(name[0:nameIndex])
            if not name_list_each_lap:
                break
            
            lapNo_content=re.split("lap=\"",html_content)
            lapNo_list_each_lap=list()
            for lapNo in lapNo_content[1:]:
                lapNoIndex=lapNo.find("\"")
                lapNo_list_each_lap.append(int(lapNo[0:lapNoIndex]))
            lap_content=re.split("time=\"",html_content)
            lap_list_each_lap=list()
            for lap in lap_content[1:]:
                lapIndex=lap.find("\"")
                lap_list_each_lap.append(lap[0:lapIndex])
            name_list_each_race.append(name_list_each_lap)
            lapNo_list_each_race.append(lapNo_list_each_lap)
            lap_list_each_race.append(lap_list_each_lap)
        counter1=0
        name_list_season.append(name_list_each_race)
        lapNo_list_season.append(lapNo_list_each_race)
        lap_list_season.append(lap_list_each_race)
        
        
    max_verstappen_object_list=list()
    hamilton_object_list=list()
    bottas_object_list=list()
    gasly_object_list=list()
    norris_object_list=list()
    ricciardo_object_list=list()
    alonso_object_list=list()
    stroll_object_list=list()
    sainz_object_list=list()
    raikkonen_object_list=list()
    giovinazzi_object_list=list()
    ocon_object_list=list()
    vettel_object_list=list()
    tsunoda_object_list=list()
    russell_object_list=list()
    latifi_object_list=list()
    mick_schumacher_object_list=list()
    perez_object_list=list()
    mazepin_object_list=list()
    leclerc_object_list=list() 
    season=list()
    counter3=0
    for name_list_each_race in name_list_season:
        counter1=0        
        max_verstappen_object=classDriver(33,"max_verstappen")
        hamilton_object=classDriver(44,"hamilton")
        bottas_object=classDriver(77,"bottas")
        gasly_object=classDriver(10,"gasly")
        norris_object=classDriver(4,"norris")
        ricciardo_object=classDriver(3,"ricciardo")
        alonso_object=classDriver(14,"alonso")
        stroll_object=classDriver(18,"stroll")
        sainz_object=classDriver(55,"sainz")
        raikkonen_object=classDriver(7,"raikkonen")
        giovinazzi_object=classDriver(99,"giovinazzi")
        ocon_object=classDriver(31,"ocon")
        vettel_object=classDriver(5,"vettel")
        tsunoda_object=classDriver(22,"tsunoda")
        russell_object=classDriver(63,"russell")
        latifi_object=classDriver(6,"latifi")
        mick_schumacher_object=classDriver(47,"mick_schumacher")
        perez_object=classDriver(11,"perez")
        mazepin_object=classDriver(9,"mazepin")
        leclerc_object=classDriver(16,"leclerc")
        max_verstappen_laps=list()
        hamilton_laps=list()
        bottas_laps=list()
        gasly_laps=list()
        norris_laps=list()
        ricciardo_laps=list()
        alonso_laps=list()
        stroll_laps=list()
        sainz_laps=list()
        raikkonen_laps=list()
        giovinazzi_laps=list()
        ocon_laps=list()
        vettel_laps=list()
        tsunoda_laps=list()
        russell_laps=list()
        latifi_laps=list()
        mick_schumacher_laps=list()
        perez_laps=list()
        mazepin_laps=list()
        leclerc_laps=list() 

        for name_list_each_lap in name_list_each_race:
            counter2=0
  
            for name in name_list_each_lap:
                if name=="max_verstappen":
                    max_verstappen_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="hamilton":
                    hamilton_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="bottas":
                    bottas_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="gasly":
                    gasly_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="norris":
                    norris_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="ricciardo":
                    ricciardo_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="alonso":
                    alonso_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="stroll":
                    stroll_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="sainz":
                    sainz_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="raikkonen" or name=="kubica":
                    raikkonen_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="giovinazzi":
                    giovinazzi_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="ocon":
                    ocon_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="vettel":
                    vettel_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="tsunoda":
                    tsunoda_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="russell":
                    russell_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="latifi":
                    latifi_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="mick_schumacher":
                    mick_schumacher_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="perez":
                    perez_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="mazepin":
                    mazepin_laps.append(lap_list_season[counter3][counter1][counter2])
                elif name=="leclerc":
                    leclerc_laps.append(lap_list_season[counter3][counter1][counter2])
                else:
                    print(name)
                counter2+=1
            counter1+=1
        max_verstappen_object.addLaps(max_verstappen_laps)
        hamilton_object.addLaps(hamilton_laps)
        bottas_object.addLaps(bottas_laps)
        gasly_object.addLaps(gasly_laps)
        norris_object.addLaps(norris_laps)
        ricciardo_object.addLaps(ricciardo_laps)
        alonso_object.addLaps(alonso_laps)
        stroll_object.addLaps(stroll_laps)
        sainz_object.addLaps(sainz_laps)
        raikkonen_object.addLaps(raikkonen_laps)
        giovinazzi_object.addLaps(giovinazzi_laps)
        ocon_object.addLaps(ocon_laps)
        vettel_object.addLaps(vettel_laps)
        tsunoda_object.addLaps(tsunoda_laps)
        russell_object.addLaps(russell_laps)
        latifi_object.addLaps(latifi_laps)
        mick_schumacher_object.addLaps(mick_schumacher_laps)
        perez_object.addLaps(perez_laps)
        mazepin_object.addLaps(mazepin_laps)
        leclerc_object.addLaps(leclerc_laps)
            
        max_verstappen_object_list.append(max_verstappen_object)
        hamilton_object_list.append(hamilton_object)
        bottas_object_list.append(bottas_object)
        gasly_object_list.append(gasly_object)
        norris_object_list.append(norris_object)
        ricciardo_object_list.append(ricciardo_object)
        alonso_object_list.append(alonso_object)
        stroll_object_list.append(stroll_object)
        sainz_object_list.append(sainz_object)
        raikkonen_object_list.append(raikkonen_object)
        giovinazzi_object_list.append(giovinazzi_object)
        ocon_object_list.append(ocon_object)
        vettel_object_list.append(vettel_object)
        tsunoda_object_list.append(tsunoda_object)
        russell_object_list.append(russell_object)
        latifi_object_list.append(latifi_object)
        mick_schumacher_object_list.append(mick_schumacher_object)
        perez_object_list.append(perez_object)
        mazepin_object_list.append(mazepin_object)
        leclerc_object_list.append(leclerc_object)
        counter3+=1
    season.append(max_verstappen_object_list)
    season.append(hamilton_object_list)
    season.append(bottas_object_list)
    season.append(gasly_object_list)
    season.append(norris_object_list)
    season.append(ricciardo_object_list)
    season.append(alonso_object_list)
    season.append(stroll_object_list)
    season.append(sainz_object_list)
    season.append(raikkonen_object_list)
    season.append(giovinazzi_object_list)
    season.append(ocon_object_list)
    season.append(vettel_object_list)
    season.append(tsunoda_object_list)
    season.append(russell_object_list)
    season.append(latifi_object_list)
    season.append(mick_schumacher_object_list)
    season.append(perez_object_list)
    season.append(mazepin_object_list)
    season.append(leclerc_object_list)
    return season

def lapTimeVariability(raceResults:list()):
    standardDev=list()
    lapCounter=list()
    lapDifferenceAll=list()
    sumLapCounter=list()
    for driver in raceResults:
        raceList=list()
        lapCounterDriver=list()
        lapDifference=list()
        for race in driver:
            lapsDifferenceAsInt=list()
            for i in range (2,len(race.lapTimes)):
                if convertStringToMilliseconds(race.lapTimes[i])<120000 and convertStringToMilliseconds(race.lapTimes[i-1])<120000:
                    if convertStringToMilliseconds(race.lapTimes[i])-convertStringToMilliseconds(race.lapTimes[i-1])<3500 and convertStringToMilliseconds(race.lapTimes[i])-convertStringToMilliseconds(race.lapTimes[i-1])>-3500:
                        lapsDifferenceAsInt.append(abs(convertStringToMilliseconds(race.lapTimes[i])-convertStringToMilliseconds(race.lapTimes[i-1])))
            if len(lapsDifferenceAsInt)<2:
                raceList.append(None)
            else:
                lapDifference.append(lapsDifferenceAsInt)
                raceList.append(statistics.stdev(lapsDifferenceAsInt))
            lapCounterDriver.append(len(lapsDifferenceAsInt))
        lapDifferenceAll.append(lapDifference)
        lapCounter.append(lapCounterDriver)
        sumLapCounter.append(sum(lapCounterDriver))
        standardDev.append(raceList)
    counter1=0
    resultStandard=list()
    for standardD in standardDev:
        counter2=0
        divider=0
        denominator=0
        missing=0
        for standard in standardD:
            if standard is not None:
                divider+=(lapCounter[counter1][counter2]-1)*standard*standard
                denominator+=lapCounter[counter1][counter2]
                missing+=1
            else:
                print("deneme")
            counter2+=1
        denominator=denominator-missing
        standardd=math.sqrt(divider/denominator)
        resultStandard.append(standardd)
        counter1+=1
    return resultStandard