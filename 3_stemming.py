# removes stems like "ing", "er", "or" from words in a sentence


# package- nltk.stem, libraries -PorterStemmer

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example = "She was driving the car in the morning and took her lunch after that"

words = word_tokenize(example)

for w in words:
	print(ps.stem(w)) 
