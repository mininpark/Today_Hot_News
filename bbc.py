from bs4 import BeautifulSoup as soup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv
import os
from urllib.parse import urlparse


URL = "https://www.bbc.com"
dirname = os.path.dirname(os.path.abspath(__file__))
csvfilename = os.path.join(dirname, 'output_bbc.csv')


def bbc_scrapper():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)
    driver.get(URL)
    links = []
    headlines = []

    # print(indeed_result.text) --> to scrap all HTML Text
    # INSTEAD OF THIS, I will scrap with BEAUTIFULSOUP for seeing the html text I have
    #soup = BeautifulSoup(result.content, "lxml")
    page = driver.page_source
    page_soup = soup(page, 'html.parser')

    def sec1():
        s1 = page_soup.find_all("a", {"class":"media__link"})
        #URL_new = "https://www.bbc.com"
        for s in s1:
            href = s.attrs['href']
            href_n = urlparse(href)
            href_new = href_n._replace(scheme='https', netloc='www.bbc.com')
            url = (href_new.geturl()) # https://velog.io/tags

            links.append(url)
            
            #strip for getting rid of unnecessary spaces
            headline_text = s.get_text().strip()           
            headlines.append(headline_text)

        dict_bbc = [
            {'headline': headlines, 'url': links} 
            for links, headlines 
            in zip(links, headlines)]    
    
        def save_csv_bbc():
            keys = dict_bbc[0].keys()   

            output_file = open(csvfilename, 'w', newline='')
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(dict_bbc)
            output_file.close()

        save_csv_bbc()
    
    driver.close()
    
    sec1()
    
#bbc_scrapper()


    # For keeping simple, I would chosse only the above headlines
    # def sec2():
    #     s2 = page_soup.find_all("a", {"class":"top-list-item__link"})

    #     for s in s2:
    #         links = []
    #         URL_new = "https://www.bbc.com"
    #         for i in s2:
    #             href = i.attrs['href']
    #             links.append(URL_new+href)

    #         headline_text = s.find("h3", {"class":"top-list-item__headline"}).get_text()
    #         #headline_text = headline.get_text()
    #         headlines = []
    #         headlines.append(headline_text)

        
    #         dict_bbc2 = dict.fromkeys(links, headline_text)
    #         print(dict_bbc2)
    
    # sec2()
        