from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

page=urllib.request.urlopen("https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29")
soup=BeautifulSoup(page,"html.parser")


# prod_name=soup.find('div',class_="_2WkVRV")
# price=soup.find('div',class_="_30jeq3")


pname=[]
pprice=[]
# pname.append(prod_name.text)
# pprice.append(price.text)

for i in soup.find_all('div',class_="_3pLy-c row"):
    getProdName=i.find('div',attrs={"class":"_4rR01T"})
    getPrice=i.find('div',attrs={"class":"_1_WHN1"})

    pname.append(getProdName.text)
    pprice.append(getPrice.text)
data=pd.DataFrame({'ProductName':pname,'ProductPrice':pprice})

print(data.head())
data.to_csv("Prod_result.csv")
