# Instead of Python Basic Library urllib --> I use more powerful Libaray "REQUESTS" 
from ctypes import resize
import pip._vendor.requests as requests
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import lxml

URL = "https://edition.cnn.com/"

#result = requests.get(URL)
# Only with BeatifulSoup I couldn't get the result, which was using by Java Script
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)

# print(indeed_result.text) --> to scrap all HTML Text
# INSTEAD OF THIS, I will scrap with BEAUTIFULSOUP for seeing the html text I have
#soup = BeautifulSoup(result.content, "lxml")
page = driver.page_source
page_soup = soup(page, 'html.parser')


headlines= []
sections = page_soup.find_all('span', {"class":"cd__headline-text"})
for section in sections:
    headlines.append(section.string)

# the first 7 elements are not relevant as headlines
im_headlines = headlines[7:]
print(im_headlines)
