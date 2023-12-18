import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split # function for splitting data to train and test sets
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.classify import SklearnClassifier
from nltk.stem import PorterStemmer, WordNetLemmatizer

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt


folder_path = 'qualifications'
data = []
keywords = ''

# Set up array of keywords
keywords = []
with open('keywords.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    # Remove newline characters at the end of each line
    cleaned_line = line.strip()
    keywords.append(cleaned_line)

# Only parses the text for keywords
def clean_text_keywords_only(text):
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.upper() in keywords]
    processed_text = ' '.join(filtered_words)
    return processed_text

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)        
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            cleaned_content = clean_text_keywords_only(file_content)
            data.append({'content': cleaned_content})

df = pd.DataFrame(data)

def wordcloud_draw(data, color = 'black'):
    words = ' '.join(data)
    cleaned_word = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and not word.startswith('#')
                                and word != 'RT'
                            ])
    wordcloud = WordCloud(stopwords=STOPWORDS,
                      background_color=color,
                      width=2500,
                      height=2000
                     ).generate(cleaned_word)
    plt.figure(1,figsize=(13, 13))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

    

wordcloud_draw(df['content'])
