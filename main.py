import requests
from bs4 import BeautifulSoup
import pandas as pd
datalist=[]
urls=['https://www.daraz.com.np/products/apple-macbook-air-13-in-with-m1-chip256gb-with-1-year-insurance-breakageliquid-damage-evostore-i105118187-s1026752551.html?spm=a2a0e.searchlistcategory.list.1.4231383a4vH83b&search=1']

for url in urls:
    response=requests.get(url)
    html_content=response.content

    soup=BeautifulSoup(html_content,'html.parser')
    
    
    Price=soup.find('div',{"class":'pdp-product-price'}).find('span',{"class":'pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl'}).text.strip()
    data={
        'Price':Price
    }
    datalist.append(data)
df=pd.DataFrame(datalist)
df.to_csv('daraz.csv',index=True)