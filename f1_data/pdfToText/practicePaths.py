def getPracticePaths():

    maps=["brn","ita","por","esp","mon","aze","fra","aut","aut","gbr","hun","bel","ned","ita","rus","tur","usa","mex","bra","qat","ksa","uae"]
    allPractice=[]
    for i in range(1,23):
        headOfPath="C:\\Bitirme_Projesi\\f1_data\pdf\\"
        if(i<10):
            headOfPath=headOfPath+"0"
        mapPractice=[]
        for j in range(1,4):
            path=headOfPath+str(i)+"_"+maps[i-1]+"_practice_"+str(j)+"_laptimes.pdf"
            if path=="C:\\Bitirme_Projesi\\f1_data\pdf\\10_gbr_practice_2_laptimes.pdf" or path=="C:\\Bitirme_Projesi\\f1_data\pdf\\10_gbr_practice_3_laptimes.pdf" or path=="C:\\Bitirme_Projesi\\f1_data\pdf\\14_ita_practice_2_laptimes.pdf" or  path=="C:\\Bitirme_Projesi\\f1_data\pdf\\14_ita_practice_3_laptimes.pdf"  or  path=="C:\\Bitirme_Projesi\\f1_data\pdf\\15_rus_practice_3_laptimes.pdf" or path=="C:\\Bitirme_Projesi\\f1_data\\pdf\\19_bra_practice_3_laptimes.pdf":
                mapPractice.append(None)
            else:
                mapPractice.append(path)
        allPractice.append(mapPractice)
    return allPractice
