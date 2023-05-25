# import section
import requests
import pandas as p
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles&requestId=c3568ff8-cbf3-495a-83ba-65f4d3bd745c")
soup=BeautifulSoup(response.content,"html.parser")

names=soup.find_all('div',class_="_4rR01T")
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)


prices=soup.find_all('div',class_="_30jeq3 _1_WHN1")
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d[1:])



rates=soup.find_all('div',class_="_3LWZlK")
rate=[]
for i in rates[0:20]:
    d=i.get_text()
    rate.append(float(d))



images=soup.find_all('img',class_="_396cs4")
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)



links=soup.find_all('a',class_="_1fQZEK")
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com"+i['href']
    link.append(d)

df=p.DataFrame()
df['Mobile_Names']=name
df['Mobile_Prices']=price
df['Mobile_Ratings']=rate
df['Mobile_Images']=image
df['Mobile_Links']=link
df.to_csv("Mobiles_data.csv")