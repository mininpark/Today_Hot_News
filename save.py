from cnn import cnn_scrapper as get_cnn_headlines
from bbc import bbc_scrapper as get_bbc_headlines

import os
import pandas as pd

dirname = os.path.dirname(os.path.abspath(__file__))

cnn_headlines = get_cnn_headlines()
bbc_headlines = get_bbc_headlines()

# to mearchge dictionaries from both scrappers
csv_cnn = csvfilename = os.path.join(dirname, 'output_cnn.csv')
csv_bbc = csvfilename = os.path.join(dirname, 'output_bbc.csv')


# CSV file written with Python has blank lines between each row mode: w-->wb
f1 = pd.read_csv(csv_cnn, header=None)
f2 = pd.read_csv(csv_bbc, header=None)
merged = pd.concat([f1, f2])
merged.to_csv('combined.csv', index=None, header=None)

#saving csv (Comma sperated values)

# checklist

# eliminate the duplicated url adresses
# find most frequent words in headlines
