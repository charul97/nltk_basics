# removes words like "of", "the", "is", etc from the sentence

# package- nltk.corpus, libraries -stopwords


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "this is charul and i am 20 years old. what is your name and age?"

x= set(stopwords.words("english"))
x.add('.')    # to remove "." also from the sentence
x.add('?')    # to remove "?" also from the sentence

word = word_tokenize(example)

filtered = []

for y in word:
	if y not in x:
		filtered.append(y)
		
print(filtered)
