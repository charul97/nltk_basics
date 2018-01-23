# WordNet is a lexical database for the English language, which was created by Princeton, and is part of the NLTK corpus. You can use WordNet alongside the NLTK module to find the meanings of words, synonyms, antonyms, and more.


# packages - nltk.corpus, library- wordnet

from nltk.corpus import wordnet
syns = wordnet.synsets("good")
print(syns[0].name())    # prints the synonym with something else at the end
print(syns[0].lemmas()[0].name())    # prints just the synonym
print(syns[0].definition())    # prints the definition of the word
print(syns[0].examples())   # prints the example related to word



synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

# since we just looked up the antonym for the first lemma, but we can easily balance this buy also doing the exact same process for the term "bad."




# Wu and Palmer method to find out how much similar a word is to the other
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))


w1 = wordnet.synset('chair.n.01')
w2 = wordnet.synset('glass.n.01')
print(w1.wup_similarity(w2))


w1 = wordnet.synset('spoon.n.01')
w2 = wordnet.synset('kite.n.01')
print(w1.wup_similarity(w2))
