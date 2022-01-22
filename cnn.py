# Instead of Python Basic Library urllib --> I use more powerful Libaray "REQUESTS" 
from ctypes import resize
from bs4 import BeautifulSoup as soup
from matplotlib.cbook import print_cycles
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://edition.cnn.com/"

def cnn_scrapper():
    #result = requests.get(URL)
    # Only with BeatifulSoup I couldn't get some elements, which were using by Java Script
    #  I used selenium with webdriver for keeping stronger, but it takes too long time to loading pages
    op = webdriver.ChromeOptions()
    # i added option to not opening the browser everytime, when the selenium works
    op.add_argument('headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)
    driver.get(URL)

    # print(indeed_result.text) --> to scrap all HTML Text
    # INSTEAD OF THIS, I will scrap with BEAUTIFULSOUP for seeing the html text I have

    page = driver.page_source
    page_soup = soup(page, 'html.parser')

    articles = page_soup.find_all("div", {"class":"cd__content"})
    dict_cnn = {"url", "headline"}
    

    for article in articles:
        links_with_text = []
        headlines = []
    

        for a in article.find_all('a', href=True): 
            if a.text: 
                URL_new = "https://edition.cnn.com"
                # there are some url links with are already stated with URL, which is not included for many other extracted URLs.
                if a.text.startswith(URL_new):
                    a_new = a.text.replace('https://edition.cnn.com', '')
                    links_with_text.append(URL_new+a_new['href'])
                else:
                    links_with_text.append(URL_new+a['href'])


        headline = article.find("span", {"class":"cd__headline-text"})
        headline_text = headline.get_text()
        headlines.append(headline_text)

        dict_cnn = [
            {'headline': headlines, 'url': links_with_text} 
            for links_with_text, headlines 
            in zip(links_with_text, headlines)]

        return dict_cnn


    driver.close()

#cnn_scrapper()

