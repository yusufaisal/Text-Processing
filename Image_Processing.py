from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import *
import re

with open('Test Data/001.txt') as f:
    text = f.read()

def caseFolding(text):
    text = text.lower()
    text = re.sub(r'[^a-z]',' ',text)
    return text
# print caseFolding(text)

def tokenisasi(text):
    token = text.split()
    return token

def stopwordRemoval(token):
    stopword = [line.rstrip('\n\r') for line in open('Stopwords/stopwords_en.txt')]
    temp =[]
    for i in range(len(token)):
        if token[i] not in stopword:
            temp.append(token[i])
    return temp
def lemmatisasi(temp):
    wordLemma = WordNetLemmatizer()
    stemmer = PorterStemmer()
    tempLemma = []
    for i in range(len(temp)):
        word = stemmer.stem(temp[i])
        tempLemma.append(wordLemma.lemmatize(word))
    return tempLemma

lower_text = caseFolding(text)
token_text = tokenisasi(lower_text)
text_after_remove_stopword = stopwordRemoval(token_text)
# print len(token_text)
print len(text_after_remove_stopword)
print lemmatisasi(text_after_remove_stopword)