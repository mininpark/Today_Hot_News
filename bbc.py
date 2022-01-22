from bs4 import BeautifulSoup as soup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re


URL = "https://www.bbc.com/"

def bbc_scrapper():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)

    # print(indeed_result.text) --> to scrap all HTML Text
    # INSTEAD OF THIS, I will scrap with BEAUTIFULSOUP for seeing the html text I have
    #soup = BeautifulSoup(result.content, "lxml")
    page = driver.page_source
    page_soup = soup(page, 'html.parser')

    def sec1():
        s1 = page_soup.find_all("a", {"class":"media__link"})
        for s in s1:
            links = []
            for i in s1:
                href = i.attrs['href']
                links.append(href)

            headline_text = s.get_text()

        dict_bbc1 = dict.fromkeys(links, headline_text)
        print(dict_bbc1)


    sec1()

    def sec2():
        s2 = page_soup.find_all("a", {"class":"top-list-item__link"})

        for s in s2:
            links = []
            URL_new = "https://www.bbc.com"
            for i in s2:
                href = i.attrs['href']
                links.append(URL_new+href)

            headline = s.find("h3", {"class":"top-list-item__headline"})
            headline_text = headline.get_text()

            print(headline_text)
        
            dict_bbc2 = dict.fromkeys(links, headline_text)
            print(dict_bbc2)
    
    sec2()
        

    driver.close()

bbc_scrapper()