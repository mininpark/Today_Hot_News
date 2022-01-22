import csv
import os
from this import d

#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))


def save_to_file(headlines):
    with open(r'C:\Users\admin\Desktop\Programming\CODE\privat project\Web_Scrapper\headlines.csv', 'w') as file:
    #file = open(r'C:\Users\admin\Desktop\Programming\CODE\privat project\Web_Scrapper\headlines.csv', 'w')
        writer = csv.DictWriter(file)
        print(["headline", "url"])

        writer.writerow(["headline", "url"])
        for headline in headlines:
            print(headline.values())

    print(headlines)

save_to_file

        







