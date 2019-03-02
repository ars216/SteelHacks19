import nltk
nltk.download('stopwords')

question = "touch the plant that's the least nutritious"
environment = ["basil", "lemon", "power plant"]

qTokens = [t for t in question.split()]

from nltk.corpus import stopwords
stopwords.words('english')

for token in qTokens:
	if token in stopwords.words('english'):
		qTokens.remove(token)

print(qTokens)

function = " "
functWords = ["most", "least", "more", "less", "big", "small"]
commandWords = ["touch", "tap", "press"]
for token in qTokens:
	if token in functWords:
		function = token
		qTokens.remove(token)
	if token in commandWords:
		qTokens.remove(token)

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

stemmedTokens = []
for token in qTokens:
	token = stemmer.stem(token)
	stemmedTokens.append(token)

print(stemmedTokens)
