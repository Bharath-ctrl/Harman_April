from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

page=urllib.request.urlopen("https://www.flipkart.com/search?q=iphone%2013&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(page,"html.parser")

pname=[]
pprice=[]
pstar=[]
pfeatures = []

for i in soup.find_all('div',class_="_3pLy-c row"):
    getProdName=i.find('div',attrs={"class":"_4rR01T"})
    pname.append(getProdName.text)

    getPrice=i.find('div',attrs={"class":"_1_WHN1"})
    pprice.append(getPrice.text)

    getStar=i.find('li',attrs={"class":"_3LWZlK"})
    if getStar is not None:
        pstar.append(getStar.text)

    getFeatures=i.find('li',attrs={"class":"rgWa7D"})
    if getFeatures is not None:
        pfeatures.append(getFeatures.text)



data=({'ProductName':pname,'ProductPrice':pprice,'Product star rating':pstar,'Features':pfeatures})
data1=pd.DataFrame.from_dict(data,orient='index')
data1=data1.transpose()
print(data1.head())
data1.to_csv("Flipkart.csv")
