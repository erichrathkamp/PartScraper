from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import os

dirpath = os.getcwd() #Path to the current working directory
dirpath = dirpath + "/chromedriver" #Change dirpath to the path to the chromedriver application
driver = webdriver.Chrome(dirpath) #Instantiate

driver.get("https://pcpartpicker.com/products/cpu")
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element_by_tag_name('div')) #Wait until the page has loaded properly, 10 seconds at most

content = driver.page_source
pageHTML = BeautifulSoup(content, features="html.parser")


products=[]
prices=[]
ratings=[]

for item in pageHTML.find_all('div', class_='td__nameWrapper'):
	for item2 in item.children:
		print(item2)

driver.close() #Close the browser page
