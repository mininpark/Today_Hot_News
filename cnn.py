# Instead of Python Basic Library urllib --> I use more powerful Libaray "REQUESTS" 
from ctypes import resize
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://edition.cnn.com/"

def cnn_scrapper():
    #result = requests.get(URL)
    # Only with BeatifulSoup I couldn't get some elements, which were using by Java Script
    #  I used selenium with webdriver for keeping stronger and 
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)

    # print(indeed_result.text) --> to scrap all HTML Text
    # INSTEAD OF THIS, I will scrap with BEAUTIFULSOUP for seeing the html text I have
    #soup = BeautifulSoup(result.content, "lxml")
    page = driver.page_source
    page_soup = soup(page, 'html.parser')

    articles = page_soup.find_all("div", {"class":"cd__content"})

    for article in articles:
        links_with_text = []
        for a in article.find_all('a', href=True): 
            if a.text: 
                URL_new = "https://edition.cnn.com"
                # there are some url links with are already stated with URL, which is not included for many other extracted URLs.
                if a.text.startswith(tuple(URL_new)):
                    a_new = a.text.replace('https://edition.cnn.com', '')
                    links_with_text.append(URL_new+a_new['href'])
                else:
                    links_with_text.append(URL_new+a['href'])
                #if "https://edition.cnn.com" is in a:

        #if "https://edition.cnn.com" in links_with_text:

        headline = article.find("span", {"class":"cd__headline-text"})
        headline_text = headline.get_text()

        dict_cnn = dict.fromkeys(links_with_text, headline_text)
        print(dict_cnn)


    driver.close()

cnn_scrapper()
#    sections = page_soup.find_all('span', {"class":"cd__headline-text"})
#for section in sections:
#    headlines.append(section.string)

# the first 7 elements are not relevant as headlines
#im_headlines = headlines[7:]
#print(im_headlines)
