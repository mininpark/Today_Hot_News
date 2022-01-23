from cnn import cnn_scrapper as get_cnn_headlines
from bbc import bbc_scrapper as get_bbc_headlines
import csv



cnn_headlines = get_cnn_headlines()
bbc_headlines = get_bbc_headlines()


# to mearchge dictionaries from both scrappers
reader = csv.reader(open("output_bbc.csv"))
reader1 = csv.reader(open("output_cnn.csv"))
# CSV file written with Python has blank lines between each row mode: w-->wb
f = open("combined.csv", "w", newline='')
writer = csv.writer(f)

for row in reader:
    writer.writerow(row)
for row in reader1:
    writer.writerow(row)

f.close()
#saving csv (Comma sperated values)

