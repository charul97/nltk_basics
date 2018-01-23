# The NLTK corpus movie_reviews data set has the reviews, and they are labeled already as positive or negative. This means we can train and test with this data.

# library - random
# package - nltk.corpus, library - movie_reviews

import nltk
import random
from nltk.corpus import movie_reviews

documents = []
for category in movie_reviews.categories():
	for fileid in movie_reviews.fileids(category):
		documents.extend([list(movie_reviews.words(fileid)), category])     #In each category (we have pos or neg), take all of the file IDs (each review has its own ID), then store the word_tokenized version (a list of words) for the file ID, followed by the positive or negative label in one big list. 

random.shuffle(documents)  #we use random to shuffle our documents. This is because we're going to be training and testing. If we left them in 								order, chances are we'd train on all of the negatives, some positives, and then test only against positives. We 							don't want that, so we shuffle the data.
		
all_words=[]
for w in movie_reviews.words():
	all_words.append(w.lower())   # changing all the words in lower case so that we don't have any issue with any word regarding to its case		
	
all_words = nltk.FreqDist(all_words)  # frequency ditribution
print(all_words.most_common(15))	

print(all_words["stupid"])  # tells the occurence of stupid
print(all_words["good"]) 
print(all_words["charul"]) 
print(all_words["aditya"]) 



word_features = list(all_words.keys())[:30]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets =[]
for rev, category in documents:
	featuresets.extend([find_features(rev), category])
# featuresets = [(find_features(rev), category) for (rev, category) in documents]    
    
# print((find_features(movie_reviews.words('pos/cv000_29590.txt'))))
# featuresets = [(find_features(rev), category) for (rev, category) in documents]      
    
    
    
    
    
