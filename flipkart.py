import pandas as pd
import requests
from bs4 import BeautifulSoup
product_name =[]
prices =[]
description =[]
reviews =[]
""" source=requests.get('https://www.flipkart.com/search?q=mobile%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
soup=BeautifulSoup(source.text,'lxml')
box=soup.find("div",class_="_1YokD2 _3Mn1Gg")
#print(soup)
np=box.find("a",class_='_1LKTO3').get('href')
#print(np)
cnp="https://www.flipkart.com/"+np
#print(cnp) """
for i in range(1,5): 
    url="https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r=requests.get (url)   
    soup=BeautifulSoup(r.text,"lxml")
    box=soup.find("div",class_="_1YokD2 _3Mn1Gg") 
   # np=box.find("a",class_='_1LKTO3').get('href')
    #print(np)
    #cnp="https://www.flipkart.com/"+np
    # print(cnp)
    desc=box.find_all("ul",class_="_1xgFaf")
    for i in desc:
      name=i.text
      description.append(name)
      #print(description)
    product=box.find_all("div",class_="_4rR01T")
    for i in product:
      name=i.text
      product_name.append(name)
    #print(len(product_name))
    price=box.find_all("div",class_="_30jeq3 _1_WHN1")
    for i in price:
      name=i.text
      prices.append(name)
    #print(len(prices))
    review=box.find_all("div",class_="_3LWZlK")
    for i in review:
      name=i.text
      reviews.append(name)
    #print(len(reviews))
    break;
df = pd.DataFrame({"Product Name": product_name, "Prices": prices, "Description": description, "Reviews": reviews})
#print(df)
df.to_csv("flipkart.csv", index=False)
#print(len(reviews), len(prices), len(product_name), len(description))