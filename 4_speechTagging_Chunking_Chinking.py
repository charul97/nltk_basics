# to declare words in a speech to be noun, pronoun, adverb, verb, etc


# package- nltk.tokenize, libraries -PunktSentenceTokenizer
# package- nltk.corpus, libraries -state_union
# libraries - tkinter


import nltk
import tkinter
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = "Hi i am charul "
sample_text = "charul agrawal is sleeping right now and disturbing sakshi"

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content() :
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			print(tagged)
			
# Chunking in Natural Language Processing (NLP) is the process by which we group various words together by their part of speech tags. 
			
			
			chunkGram = r"""Chunk: {<NN.?>?} """
			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)
			print(chunked)
			chunked.draw()
			

# Chinking is a part of the chunking process with natural language processing with NLTK. A chink is what we wish to remove from the chunk. We define a chink in a very similar fashion compared to how we defined the chunk. 

			chunkGram= r"""Chunk: {<.*>+}
						} <VB|IN>+ { """  # curly braces in opposite faishon for chinking
			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)
			print(chunked)
			chunked.draw()					
		
	except Exception as e:
		print(str(e))
		
process_content()			



'''	Modifiers
    {1,3} = for digits, u expect 1-3 counts of digits, or "places"
    + = match 1 or more
    ? = match 0 or 1 repetitions.
    * = match 0 or MORE repetitions
    $ = matches at the end of string
    ^ = matches start of a string
    | = matches either/or. Example x|y = will match either x or y
    [] = range, or "variance"
    {x} = expect to see this amount of the preceding code.
    {x,y} = expect to see this x-y amounts of the precedng code
'''







"""	
No. Tag Description
1. 	CC 	Coordinating conjunction
2. 	CD 	Cardinal number
3. 	DT 	Determiner
4. 	EX 	Existential there
5. 	FW 	Foreign word
6. 	IN 	Preposition or subordinating conjunction
7. 	JJ 	Adjective
8. 	JJR Adjective, comparative
9. 	JJS	Adjective, superlative
10. LS 	List item marker
11.	MD 	Modal
12 	NN 	Noun, singular or mass
13.	NNS	Noun, plural
14.	NNP	Proper noun, singular
15.	NNPS Proper noun, plural
16.	PDT	Predeterminer
17.	POS	Possessive ending
18.	PRP	Personal pronoun
19.	PRP$ Possessive pronoun
20.	RB 	Adverb
21.	RBR Adverb, comparative
22.	RBS Adverb, superlative
23.	RP 	Particle
24.	SYM Symbol
25.	TO 	to
26.	UH 	Interjection
27.	VB 	Verb, base form
28.	VBD Verb, past tense
29.	VBG Verb, gerund or present participle
30.	VBN Verb, past participle
31.	VBP Verb, non-3rd person singular present
32.	VBZ Verb, 3rd person singular present
33.	WDT Wh-determiner
34.	WP 	Wh-pronoun
35.	WP$ Possessive wh-pronoun
36.	WRB Wh-adverb 
"""


