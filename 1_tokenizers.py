# separates words and sentences

# package- nltk.tokenize, libraries -sent_tokenize, word_tokenize

 
from nltk.tokenize import sent_tokenize, word_tokenize

# tokenizing  - word tokenizers, sentence tokenizers
# lexicon and corporas
# corpora - body of text. ex: medical journals, presidential speeches, English language
# lexicon - words and their meanings

example = "Hi this is charul. What is your name? what is your age? "
print(sent_tokenize(example))
print(word_tokenize(example))
