import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import CountVectorizer
import os

with open("keywords_large_set.txt") as f:
    vocab = [i.lower().strip() for i in f.readlines()]

vocab = set(vocab)

cv = CountVectorizer(vocabulary=vocab)
corpus = []

d1 = pd.read_csv("countables.csv", delimiter=";")
d1 = d1.sort_values("jobID")

print(pd.unique(d1["Seniority level"]))

ids = d1[d1["Seniority level"] == "Internship"]
print(ids)

for i in sorted(os.listdir("qualifications")):
    with open(os.path.join("qualifications",i)) as f:
        corpus.append(f.read().strip())

X = cv.fit_transform(corpus).toarray()
qualifications = pd.DataFrame(X, columns=cv.get_feature_names_out())


