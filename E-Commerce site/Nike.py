from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome(r"D:\Python Project\Selenium\chromedriver")
products=[] #List to store name of the product
prices=[] #List to store price of the product
Descriptions=[] #List to store rating of the product
driver.get("https://www.nike.com/w/womens-lifestyle-shoes-13jrmz5e1x6zy7ok")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.find_all('a',href=True, attrs={'class':'product-card__link-overlay'}):
    name = a.find('div', attrs={'class':'product-card__title'})
    price=a.find('div', attrs={'class':'product-card__price'})
    products.append(name.text)
    prices.append(price.text)
    Descriptions=a.find('li', attrs={'class':'product-card__subtitle'}) 
    #ratings.append(rating.text) 
df = pd.DataFrame({'Product Name':products,'Price':prices, 'Description' :Descriptions}) 
#,'Rating':ratings
df.to_csv('scraping .csv', index=False, encoding='utf-8')
