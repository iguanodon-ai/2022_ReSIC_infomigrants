import os, sys
import pandas as pd
import hashlib
import json, math
from tqdm import tqdm

DATA_WORK = os.path.join("data", "work")
DATA_FINAL = os.path.join("data", "final")
PATHS = [DATA_WORK, DATA_FINAL]

with open("authors.json") as f:
    AUTHOR_KEY = json.load(f)

for path in PATHS:
    os.makedirs(path, exist_ok=True)

def get_hash(string):
    hash_object = hashlib.md5(string.encode()) # assuming utf8
    return hash_object.hexdigest()

def get_author(name):
    name = str(name)
    return AUTHOR_KEY[name]

def clean_date(date):
    date = str(date)
    if len(date) == 3:
        return "NO_DATE"
    date = date.replace("Published on : ", "")
    date = date.strip()
    return date
    #YEARMONTH = "/".join(date.split("/")[0:2])
    #return YEARMONTH

blacklist = [
    "First published: ",
    "First published ",
    "© Copyright",
    "DW is not responsible for the content of external websites",
    "dw.com)"
]

bl_remove = [
    "(Source:",
    "Click to read more",
    "Click\xa0\xa0to read more. here",
    "More articles"
]

def clean_string(string):
    string = str(string)
    string = string.split("Author: ", 1)[0]
    for bl in bl_remove:
        string = string.replace(bl, "")
    l = string.split("\n")
    l2 = [s for s in l if not any(bl in s for bl in blacklist)]
    string = "\n".join(l2)
    return string

def clean_title(string):
    string = str(string)
    for bl in bl_remove:
        string = string.replace(bl, "")
    return string

def check_nan(val):
    try:
        val = float(val)
        if math.isnan(val):
            return True
        else:
            return False
    except ValueError:
        return False


class Corpus_creator():
    def __init__(self, data):
        self.data = data
        
    def load_data(self):
        df = pd.read_csv(os.path.join(DATA_WORK, self.data))
        df = df.sort_values(by = 'web-scraper-order')

        return df

    def parse(self, df):
        x = 0
        data = {}
        for URL in df["link-href"].unique():
            data[URL] = {
                "country" : [],
                "text" : [],
                "date" : [],
                "author": [],
                "category" : [],
                "titre" : []
            }
            df_temp = df[df["link-href"] == URL]
            for i, row in df_temp.iterrows():

                if not check_nan(row["titre"]):
                    title = clean_title(row["titre"])
                    data[URL]["titre"].append(title)

                data[URL]["country"].append(row["pays"])

                if not check_nan(row["text"]):
                    texte = clean_string(row["text"])
                    data[URL]["text"].append(texte)
                
                date = clean_date(row["date"])
                data[URL]["date"].append(date)
                
                author = get_author(row["author"])
                data[URL]["author"].append(author)
                
                data[URL]["category"].append(row["catégorie"])
            
        return data

    
    def write_to_file(self, data):
        with open(os.path.join(DATA_FINAL, self.data.replace(".csv", ".txt")), "w") as f:
            print("#### Writing to file....")
            for URL in tqdm(data):
                date = data[URL]["date"][0]
                author = data[URL]["author"][0]
                cat = data[URL]["category"][0]
                pays = data[URL]["country"][0]
                texte = "\n".join(data[URL]["titre"])+"\n"
                texte += " ".join(data[URL]["text"])
                texte = texte.replace("*","")


                content = f"**** *article_{get_hash(URL)} *date_{date} *date-mois_{date[:7]} *auteur_{author} *pays_{pays} *catégorie_{cat} *URL_{URL}"
                content += f"\n\n{texte}\n\n"
                f.write(content)
            print("#### Done.")



    
