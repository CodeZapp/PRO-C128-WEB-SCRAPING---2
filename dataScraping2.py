
from turtle import distance
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(url)
soup = bs(page.text, 'html.parser')
starTable = soup.find_all('table')
tempList = []
tableRows = starTable[7].find_all('tr')
for tr in tableRows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)
starNames = []
distance = []
mass = []
radius = []
for i in range(1, len(tempList)):
    starNames.append(tempList[i][0])
    distance.append(tempList[i][5])
    mass.append(tempList[i][7])
    radius.append(tempList[i][8])
df2 = pd.DataFrame(list(zip(starNames, distance, mass, radius)), columns = ['Star names', 'Distance', 'Mass', 'Radius'])
print(df2)
df2.to_csv('dwarfStars.csv')