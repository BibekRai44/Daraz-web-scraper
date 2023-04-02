from selenium import webdriver
import pandas as pd
driver_path='/Users/bibekrai/workspace/Daraz web scrapper/chromedriver'
datalist=[]
url=['https://www.daraz.com.np/products/apple-macbook-air-13-in-with-m1-chip256gb-with-1-year-insurance-breakageliquid-damage-evostore-i105118187-s1026752551.html?spm=a2a0e.searchlistcategory.list.1.4231383a4vH83b&search=1']
driver = webdriver.Chrome(driver_path)
driver.get(url)

price_element = driver.find_element_by_xpath('//div[@class="pdp-product-price"]//span[@class="pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl"]')
price=price_element.text.strip()
data={
    'Price':price
}
datalist=[data]
df = pd.DataFrame(datalist)

df.to_csv('daraz.csv', index=True)

driver.quit()