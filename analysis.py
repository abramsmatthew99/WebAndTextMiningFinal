import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import CountVectorizer
import os
from make_wordcloud import wordcloud_draw, clean_text_keywords_only

with open("keywords.txt") as f:
    vocab = [i.lower().strip() for i in f.readlines()]

vocab = set(vocab)
keywords = list(vocab)

cv = CountVectorizer(vocabulary=vocab)
corpus = []

d1 = pd.read_csv("countables.csv", delimiter=";")
d1 = d1.sort_values("jobID")

ids = d1[d1["Seniority level"] == "Internship"]
internships = [f"qualifications/{i}_qualifications.txt" for i in ids[["jobID"]].values.flatten().tolist()]

for i in internships:
    if os.path.exists(i):
        with open(i) as f:
            corpus.append(f.read().strip())

data = []
for i in internships:
    if os.path.exists(i):
        with open(i, 'r', encoding='utf-8') as file:
            file_content = file.read()
            #cleaned_content = ' '.join([word for word in file_content.split() if word in vocab])
            cleaned_content = clean_text_keywords_only(file_content, keywords=list(vocab))
            #print(cleaned_content)
            data.append({'content': cleaned_content})

df = pd.DataFrame(data)
wordcloud_draw(df['content'], filename='internships')

X = cv.fit_transform(corpus).toarray()
qualifications = pd.DataFrame(X, columns=cv.get_feature_names_out())

#print(qualifications)

corpus = []
ids = d1[d1["Seniority level"] == "Entry level"]
jobs = [f"qualifications/{i}_qualifications.txt" for i in ids[["jobID"]].values.flatten().tolist()]

for i in jobs:
    if os.path.exists(i):
        with open(i) as f:
            corpus.append(f.read().strip())

data = []
for i in jobs:
    if os.path.exists(i):
        with open(i, 'r', encoding='utf-8') as file:
            file_content = file.read()
            #cleaned_content = ' '.join([word for word in file_content.split() if word in vocab])
            cleaned_content = clean_text_keywords_only(file_content, keywords=list(vocab))
            #print(cleaned_content)
            data.append({'content': cleaned_content})

df = pd.DataFrame(data)
wordcloud_draw(df['content'], filename='entrylevel')

levels = d1[["Seniority level"]]
d2 = pd.DataFrame(levels.value_counts())
d2 = d2.drop(["Contract","Executive","Part-time","Other","Temporary"])
d2["title"] = d2.index
d2 = pd.concat([pd.DataFrame({"count":[225],"title":["Other"]}),d2], ignore_index=True)
d2.set_index("title",  inplace=True)
#print(d2)
d2.plot.pie(subplots=True,legend=False)[0].get_figure().savefig("levels")
