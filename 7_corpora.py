# corpora is just a body of texts. Generally, corpora are grouped by some sort of defining characteristic.

# package- nltk.corpus, libraries - gutenberg


import nltk
print(nltk.__file__)   # to know the location of nltk


from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import gutenberg

# sample text
sample = gutenberg.raw("bible-kjv.txt")    # text files are present in nltk_data 
sample2 = gutenberg.raw("austen-sense.txt")

tok = sent_tokenize(sample)
tok2 = sent_tokenize(sample2)

for x in range(5):
    print(tok[x])
    
for x in range(5):
    print(tok2[x])    
