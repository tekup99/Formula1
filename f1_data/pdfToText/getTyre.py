# importing the libraries
from bs4 import BeautifulSoup
import requests
import re
def getTyre(link):
    url=link
    if url=="https://press.pirelli.com/2021-belgian-grand-prix---sunday/": 
        return None
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    text=soup.prettify()
    pitStopIndexStart=text.find("PIT STOP SUMMARY")
    text=text[pitStopIndexStart:len(text)-1]
    pitStopIndexFinish=text.find("n = new | u = used")
    table=text[0:pitStopIndexFinish]
    text2=re.split('<tr align="center">\n',text)

    driver=[]
    driverNo=[]
    driverName=[]
    driverTyreChoices=[]
    firstDriver=int
    for i in range (0,len(text2)):
        if text2[i].find("<td>\n")!=-1:
            firstDriver=i
            break
    for i in range (firstDriver,len(text2)):
        str=text2[i].replace("<td>","")
        str=str.replace("</td>","")
        str=str.replace("<tr>","")
        str=str.replace("</tr>","")
        str=str.replace("<span>", "")
        str=str.replace("</span>", "")
        str=str.replace("\n","")
        str=str.replace("                                                   ","")
        str=str.replace("                                 ","                ")
        str=str.replace("                      ", "                ")
        str=str.replace("                    ", "                ")
        if(i==len(text2)-1):
            str=str[0:str.find("<")]
            if url=="https://press.pirelli.com/2021-russian-grand-prix---sunday/":
                str=str[16:len(str)]
        if url!="https://press.pirelli.com/2021-russian-grand-prix---sunday/":
            str=str[16:len(str)]
        if url=="https://press.pirelli.com/2021-turkish-grand-prix---sunday/" and i==firstDriver:
            str=str[3:len(str)]

        driverNo.append(int(str[0:2].replace(" ", "")))
        str=str[2:len(str)]
        for j in range(0,len(str)):
            if str[j].isalpha():
                str=str[j:len(str)]
                driverName.append(str[0:3])
                break
        str=str[19:len(str)]
        tyreChoices=[]
        tyreChoices.append(str[0:8].replace("n", "").replace("u","").replace(" ",""))
        
        if url=="https://press.pirelli.com/2021-emilia-romagna-grand-prix--sunday/" or url=="https://press.pirelli.com/2021-hungarian-grand-prix---sunday/" or url=="https://press.pirelli.com/2021-russian-grand-prix---sunday/":
            str=str[18:len(str)]
        else:
            str=str[19:len(str)]
        str=str.replace("                      ", "                ")
        input=str[0:14].replace("n","").replace("u","").replace(" ","")
        if input[len(input)-1:len(input)]==")":
            input=input[0:len(input)-3].replace("(","")
        tyreChoices.append(input)
        for j in range(0,len(str)):
            if str[j]==')':
                input=str[j+15:j+22].replace("n","").replace("u","").replace(" ","")
                if input[len(input)-1:len(input)]==")":
                    input=input[0:len(input)-3].replace("(","")
                tyreChoices.append(input.replace("(",""))
        
        driverTyreChoices.append(tyreChoices)

    driver.append(driverNo)
    driver.append(driverName)
    driver.append(driverTyreChoices)

    return driver