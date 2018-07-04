def x():
    file = open("temp.txt",'w+')
    file.write('city,country,month ave: highest high,month ave: lowest low\n\
Beijing,China,30.9,-8.4\nCairo,Egypt,34.7,1.2\nLondon,UK,23.5,2.1\
\nNairobi,Kenya,26.3,10.5\nNew York City,USA,28.9,-2.8\nSydney,Australia,26.5,8.7\nTokyo,Japan,30.8,0.9\n')
    file.close()




    file=open("temp.txt",'a+')
    file.write("Rio de Janeiro,Brazil,30.0,18.0\n")
    file.seek(0)
    headings=file.readline()
    headingsList=headings.split(',')
    headingsList[0]="City"
    listForAppend=headingsList[0:1]
    listForAppend.append("of")
    listForAppend.extend(headingsList[1:])
    listForAppend[4]="is"
    listForAppend.append("temp")
    listForAppend.append("Celsius")
    cityTemp=file.readline()
    while cityTemp:
        city_temp=cityTemp
        cityTemp=file.readline()
        listCityTemp=city_temp.split(',')
        listForAppend[2]=listCityTemp[0]
        listForAppend[5]=listCityTemp[2]
        result=" ".join(listForAppend)
        print(result)



if __name__ == '__main__':
    x()
