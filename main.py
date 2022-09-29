from utils import *
import os, sys


DATA = "scraped.csv"


creator = Corpus_creator(DATA)
df = creator.load_data()
data = creator.parse(df)
print(len(data))
creator.write_to_file(data)
