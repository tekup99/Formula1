import urllib.request

maps=["brn","ita","por","esp","mon","aze","fra","aut","aut","gbr","hun","bel","ned","ita","rus","tur","usa","mex","bra","qat","ksa","uae"]
practices=["first","second","third"]
i=20

for map in maps:
    j=1
    for practice in practices: 
        onlar=str(int(i/10))
        birler=str(i%10)
        pdf_path = "https://www.fia.com/sites/default/files/2021_"+onlar+birler+"_"+map+"_f1_p"+str(j)+"_timing_"+practice+"practicesessionlaptimes_v01.pdf"
        def download_file(download_url, filename):
            response = urllib.request.urlopen(download_url)    
            file = open(filename + ".pdf", 'wb')
            file.write(response.read())
            file.close()
        download_file(pdf_path, onlar+birler+"_"+map+"_"+"practice"+"_"+str(j)+"_laptimes")
        j+=1
    i+=1