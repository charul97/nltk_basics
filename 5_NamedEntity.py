# Named entity recognition is useful to quickly find out what the subjects of discussion are. NLTK comes packed full of options for us. We can find just about any named entity, or we can look for specific ones.


# NumPy is the fundamental package for scientific computing with Python. It contains among other things: a powerful N-dimensional array object. sophisticated (broadcasting) functions. It is required package for nltk.ne_chunk().



# libraries - numpy



'''
NE Type and Examples
ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian
'''


import nltk
import tkinter
import numpy
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = "Hi i am charul "
sample_text = "Obama is sleeping right now and is unaware of TajMahal because he is presently staying in NewYork city. "

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content() :
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			namedEntity= nltk.ne_chunk(tagged, binary=True)
			namedEntity.draw()
			
			
	except Exception as e:
		print(str(e))
		
process_content()			
		
