#Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.
#Some Resources:
#https://www.dataquest.io/blog/web-scraping-tutorial-python/
#https://www.edureka.co/blog/web-scraping-with-python/

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.rascto.ca/"

#Open the webpage
driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get(url)

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
forecastData = soup.find(id='skychart')
cloudCover = forecastData.find(id='cloud_cover').get_text()
transparency = forecastData.find(id='transparency').get_text()
seeing = forecastData.find(id='seeing').get_text()

checkForGo = forecastData.select("div")
info = [go.getText() for go in checkForGo if 'GO' in go.getText()]
if len(info) != 0:
    gonogo = "GO"
else:
    gonogo ="NO GO"

#print(info)
#print(forecastData)
print("Location: ")
print("Cloud Cover: "+cloudCover)
print("Transparency: "+transparency)
print("Seeing: "+seeing)
print("----------------")
print("Call: "+gonogo)
driver.quit()