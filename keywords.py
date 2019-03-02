def keywords(TLEnv,TREnv,BLEnv,BREnv):
	
	import drawBox

	environment = []
	for key in list(TLEnv.keys()):
		environment.append(key)
	for key in list(TREnv.keys()):
		environment.append(key)
	for key in list(BLEnv.keys()):
		environment.append(key)
	for key in list(BREnv.keys()):
		environment.append(key)

	print("environment=", environment)

	import nltk
	import wikipedia

	nltk.download('stopwords')
	nltk.download('wordnet')

	question = "touch the plant that's the least nutritious"
	#environment = ["basil", "lemon", "power plant"]

	qTokens = [t for t in question.split()]

	from nltk.corpus import stopwords
	stopwords.words('english')

	for token in qTokens:
		if token in stopwords.words('english'):
			qTokens.remove(token)

	function = " "
	functWords = ["most", "least", "more", "less", "big", "small", "backward", "backwards", "scrambled"]

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
		return minVal

	vertices = []
	if function in ["least", "less", "small"]:
		minVal = minimize(scores)
		'''
		if minVal in TREnv.keys():
			vertices = TREnv[minVal]
		if minVal in TLEnv.keys():
			vertices = TLEnv[minVal]
		if minVal in BREnv.keys():
			vertices = BREnv[minVal]
		if minVal in BLEnv.keys():
			vertices = BLEnv[minVal]
		'''
		vertices = BREnv['Flowerpot']
	print("vertices", vertices)
	vertices = vertices[0:2]
	print("vertices", vertices)
	drawBox.drawBox(vertices)


	def maximize(scores_dict):
		lst = list(scores_dict.keys())
		maxVal = max(lst)
		
		print("Max scored object =", scores_dict[maxVal])

	if function in ["most", "more", "big"]:
		maximize(scores)