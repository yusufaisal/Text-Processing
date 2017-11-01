import re

with open('Test Data/001.txt') as f:
    text = f.read()

def caseFolding(text):
    text = text.lower()
    text = re.sub(r'[^a-z]',' ',text)
    return text

print caseFolding(text)