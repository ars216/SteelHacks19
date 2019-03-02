import nltk
import wikipedia

nltk.download('stopwords')
nltk.download('wordnet')

question = "touch the plant that's the least nutritious"
environment = ["basil", "lemon", "power plant"]

qTokens = [t for t in question.split()]

from nltk.corpus import stopwords
stopwords.words('english')

for token in qTokens:
	if token in stopwords.words('english'):
		qTokens.remove(token)

function = " "
functWords = ["most", "least", "more", "less", "big", "small"]
commandWords = ["touch", "tap", "press"]
for token in qTokens:
	if token in functWords:
		function = token
		qTokens.remove(token)
	if token in commandWords:
		qTokens.remove(token)

#print(qTokens)
#print("qTokens length = %d", len(qTokens))

from nltk.corpus import wordnet
synTokens = {}
for i in range(0, len(qTokens)):
	token = qTokens[i]
	synonyms = []
	for syn in wordnet.synsets(token):
		for lemma in syn.lemmas():
			synonyms.append(lemma.name())
	synTokens[token] = synonyms

#print(synTokens)
'''
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

stemmedTokens = []
for token in qTokens:
	token = stemmer.stem(token)
	stemmedTokens.append(token)

print(stemmedTokens)
'''
for obj in environment:
	#print("obj=", obj)
	score = 0
	page = wikipedia.page(obj)
	for token in synTokens:
		if token in page.content:
			score = score+1
		#print("token=", token)
	#print("score=", score)
	if score == 0:
		environment.remove(obj)

key = list(synTokens.keys())[-1]
scores = {}
for obj in environment:
	#print("obj=", obj)
	score = 0
	page = wikipedia.page(obj)
	for token in synTokens[key]:
		if token in page.content:
			score = score+1
		#print("token=", token)
	scores[score] = obj
	#print("scores=", scores)

#print("function=", function)

def minimize(scores_dict):
	lst = list(scores_dict.keys())
	minVal = min(lst)
	print("Min scored object =", scores_dict[minVal])

if function in ["least", "less", "small"]:
	minimize(scores)
