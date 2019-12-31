from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os

dirpath = os.getcwd()
dirpath = dirpath + "/chromedriver"
print(dirpath)
driver = webdriver.Chrome(dirpath)

products=[]
prices=[]
ratings=[]
driver.get("https://pcpartpicker.com/products/cpu")
content = driver.page_source
