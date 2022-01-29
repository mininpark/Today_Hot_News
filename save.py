from cnn import cnn_scrapper as get_cnn_headlines
from bbc import bbc_scrapper as get_bbc_headlines
import glob
import os
import pandas as pd


def save_csv():
    get_cnn_headlines()
    get_bbc_headlines()
    
    dirname = os.path.dirname(os.path.abspath(__file__))

    # to mearchge dictionaries from both scrappers
    files = os.path.join(dirname, '*.csv')

    # list of merged files returned
    files = glob.glob(files)

    print("Saving now...");
    # joining files with concat and read_csv
    combined_csv = pd.concat([pd.read_csv(f) for f in files]).drop_duplicates().reset_index(drop=True)
    #final_combined_csv = pd.unique(combined_csv).tolist()

    os.chdir(os.path.dirname(__file__))

    combined_csv.to_csv("combined.csv", index=False, encoding='utf-8-sig')
    #df = pd.concat(map(pd.read_csv, files), ignore_index=True)
    #print(df)

#save_csv()

# checklist

# eliminate the duplicated url adresses
# find most frequent words in headlines
