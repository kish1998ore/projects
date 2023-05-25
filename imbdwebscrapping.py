import requests
import pandas 
from bs4 import BeautifulSoup

responce=requests.get('https://www.imdb.com/chart/top/')
#print(responce)
soup=BeautifulSoup(responce.content,'html.parser')
#print(soup)


titles=soup.find_all('td',class_='titleColumn')
title=[]
for i in titles[0:22]:
    d=i.get_text()
    title.append(d)
#print(title)    

ratings=soup.find_all('td',class_='ratingColumn imdbRating')
rating=[]
for i in ratings[0:22]:
    d=i.get_text()
    rating.append(d)
#print(rating)   

movielist=pandas.DataFrame()
movielist['titles']=title
movielist['ratings']=rating
movielist.to_csv("movielist.csv")



