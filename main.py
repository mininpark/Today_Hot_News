from cnn import cnn_scrapper as get_cnn_headlines
from bbc import bbc_scrapper as get_bbc_headlines
from save import save_to_file
from collections import ChainMap


cnn_headlines = get_cnn_headlines()
#bbc_headlines = get_bbc_headlines()

headlines = cnn_headlines
# to mearchge dictionaries from both scrappers

#saving csv (Comma sperated values)
save_to_file(headlines)



