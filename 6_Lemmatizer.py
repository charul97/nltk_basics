# A very similar operation to stemming is called lemmatizing. The major difference between these is, as you saw earlier, stemming can often create non-existent words.


# package- nltk.stem, libraries - WordNetLemmatizer

from nltk.stem import WordNetLemmatizer

lemmatizer= WordNetLemmatizer()

print(lemmatizer.lemmatize("anger"))
print(lemmatizer.lemmatize("morning"))
print(lemmatizer.lemmatize("angers"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("better",pos="a")) # pos="a" means that we want an adjective for it
print(lemmatizer.lemmatize("better",pos="n")) # pos="n" means that we want a noun for it
