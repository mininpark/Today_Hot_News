from cnn import cnn_scrapper as get_cnn_headlines
from bbc import bbc_scrapper as get_bbc_headlines

import os
import pandas as pd

dirname = os.path.dirname(os.path.abspath(__file__))
csvfilename = os.path.join(dirname, 'combined.csv')
csv_cnn = csvfilename = os.path.join(dirname, 'output_cnn.csv')
csv_bbc = csvfilename = os.path.join(dirname, 'output_bbc.csv')


cnn_headlines = get_cnn_headlines()
bbc_headlines = get_bbc_headlines()

dirname = os.path.dirname(os.path.abspath(__file__))

# to mearchge dictionaries from both scrappers

# CSV file written with Python has blank lines between each row mode: w-->wb
f1 = pd.read_csv(csv_cnn, header=None)
f2 = pd.read_csv(csv_bbc, header=None)
merged = pd.concat([f1, f2])
merged.to_csv('combined_file.csv', index=None, header=None)

#saving csv (Comma sperated values)

# checklist

# eliminate the duplicated url adresses
# find most frequent words in headlines
