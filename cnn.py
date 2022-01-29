# Instead of Python Basic Library urllib --> I use more powerful Libaray
import os
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv
from urllib.parse import urlparse

URL = "https://edition.cnn.com"

dirname = os.path.dirname(os.path.abspath(__file__))
csvfilename = os.path.join(dirname, 'output_cnn.csv')

def cnn_scrapper():
    #result = requests.get(URL)
    # Only with BeatifulSoup I couldn't get some elements, which were using by Java Script
    #  I used selenium with webdriver for keeping stronger, but it takes too long time to loading pages
    op = webdriver.ChromeOptions()
    # i added option to not opening the browser everytime, when the selenium works
    op.add_argument('headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)
    driver.get(URL)
    links_with_text = []
    headlines = []

    # print(indeed_result.text) --> to scrap all HTML Text
    # INSTEAD OF THIS, I will scrap with BEAUTIFULSOUP for seeing the html text I have
    page = driver.page_source
    page_soup = soup(page, 'html.parser')

    articles = page_soup.find_all("div", {"class":"cd__content"})


    for article in articles:
        for a in article.find_all('a', href=True): 
            #if a.text: 
                # there are some url links with are already stated with URL, which is not included for many other extracted URLs.
            href = a.attrs['href']
            href_n = urlparse(href)
            href_new = href_n._replace(scheme='https', netloc='edition.cnn.com')
            url = (href_new.geturl()) 

            links_with_text.append(url)

        headline = article.find("span", {"class":"cd__headline-text"})
        headline_text = headline.get_text()
        headlines.append(headline_text)

    dict_cnn = [{'headline' : headlines, 'url' : links_with_text} for headlines, links_with_text in zip(headlines,links_with_text)]
    

    #Print the keys and values of the dictionary
    #print(dict_cnn)

    # csv saving   

    keys = dict_cnn[0].keys()   
    output_file = open(csvfilename, 'w', newline='')
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(dict_cnn)
    output_file.close()

    # loop over dictionary keys and values
    #for key, val in dict_cnn.items():

        # write every key and value to file
        #    w.writerow([key, val])
    
    driver.close()
#cnn_scrapper()



