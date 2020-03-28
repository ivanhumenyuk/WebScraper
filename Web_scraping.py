import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XmS5YHIzZhE')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
#print(soup.find_all('img'))
week = soup.find(id = 'seven-day-forecast-body')
#print(week)
items = (week.find_all(class_='tombstone-container'))
#print(items)
#print(items[0])

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
temps = [temp.find(class_='temp').get_text() for temp in items]
short_desc = [desc.find(class_='short-desc').get_text() for desc in items]

d = [period_names, short_desc, temps]
print(d)

for i in d:
    for j in i:
        print(j, end=' ')
    print()

weather_stuff = pd.DataFrame(
    {
        'Period': period_names,
        'Short description': short_desc,
        'Temperature': temps,
    })
print(weather_stuff)

weather_stuff.to_csv('weather.csv')