from pathlib import Path
from bs4 import BeautifulSoup
import bleach
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer as wnl

import random
import string

def get_files():
    files_list = []
    for fi in Path("Job Descriptions").iterdir():
        files_list.append(fi)
    return files_list

def clean(text):
    soup = BeautifulSoup(text, 'html.parser')
    countables = get_countables(soup)
    # Usually job descriptions and qualifications are in bold, not in a div by themselves
    bold_list = soup.find_all("strong")
    for i in range(len(bold_list)):
        bold_list[i] = bold_list[i].text
    resp_string = get_responsibilities(bold_list)
    qual_string = get_qualifications(bold_list)
    #print(resp_string)
    #print(qual_string)
    resp = ""
    qual = ""
    if resp_string:
        resp = " ".join(BeautifulSoup(str(soup).split(resp_string)[-1].split("<strong>")[0],'html.parser').stripped_strings)
        #print(resp)
    if qual_string:
        qual = " ".join(BeautifulSoup(str(soup).split(qual_string)[-1].split("<strong>")[0],'html.parser').stripped_strings).split("Show more")[0]
        #print(qual)
    return resp, qual, countables

#    print(BeautifulSoup(str(soup).split(resp_string)[1].split("<strong>")[0],'html.parser').text)

def get_countables(soup):
    countables = soup.find_all(class_="description__job-criteria-text description__job-criteria-text--criteria")
    return [i.get_text().strip() for i in countables]

def get_responsibilities(bold_list):
    #print(bold_list)
    for i in range(len(bold_list)):
        j = bold_list[i].lower().split()
        for word in j:
            word = "".join([char for char in word if char not in string.punctuation])
            word = lemmatizer.lemmatize(word)
            for synset in wn.synsets(word):
                if "responsibility" in synset.lemma_names():
                    return bold_list[i]
                if "summary" in synset.lemma_names():
                    return bold_list[i]
                if "overview" in synset.lemma_names():
                    return bold_list[i]
                if "duty" in synset.lemma_names():
                    return bold_list[i]
                if "description" in synset.lemma_names():
                    return bold_list[i]
    return ''

def get_qualifications(bold_list):
    for i in range(len(bold_list)):
        j = bold_list[i].lower().split()
        #print(bold_list[i])
        for word in j:
            word = "".join([char for char in word if char not in string.punctuation])
            word = lemmatizer.lemmatize(word)
            for synset in wn.synsets(word):
                if "skill" in synset.lemma_names():
                    return bold_list[i]
                if "requirement" in synset.lemma_names():
                    return bold_list[i]
                if "qualification" in synset.lemma_names():
                    return bold_list[i]
    return ''

if __name__ == '__main__':
    #i = random.randint(0,3000)
    #rcount, qcount, ccount = 0, 0, 0
    #r = []
    files = get_files()[:100]
    lemmatizer = wnl()
    for i in range(len(files)):
        fi = files[i]
        with fi.open() as f:
            text = ' '.join([t.strip() for t in f.readlines()])
            resp, qual, countables = clean(text)
        if resp:
            with open(f"descriptions/{fi.stem}_description.txt","w") as tx:
                tx.write(f"{resp}\n")
        if qual:
            with open(f"qualifications/{fi.stem}_description.txt","w") as tx:
                tx.write(f"{qual}\n")
        if countables:
            with open("countables.csv","a") as tx:
                tx.write(f"{','.join([fi.stem] + countables)}\n")
        print(f"Saved {fi.stem}")
