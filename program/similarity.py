from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

import nltk
import string
import os
from nltk.stem.porter import PorterStemmer

################################################################
#use NLP ways to solve the similarity problem but it will take too much time so that I prefer use the simple way (directly compare text file counting vection directly)

#path = '/opt/datacourse/data/parts'
#token_dict = {}
#stemmer = PorterStemmer()
#
#def stem_tokens(tokens, stemmer):
#	stemmed = []
#	for item in tokens:
#		stemmed.append(stemmer.stem(item))
#	return stemmed
#
#def tokenize(text):
#	tokens = nltk.word_tokenize(text)
#	stems = stem_tokens(tokens, stemmer)
#	return stems
#
#for subdir, dirs, files in os.walk(path):
#	for file in files:
#		file_path = subdir + os.path.sep + file
#		shakes = open(file_path, 'r')
#		text = shakes.read()
#		lowers = text.lower()
#		no_punctuation = lowers.translate(None, string.punctuation)
#		token_dict[file] = no_punctuation
#		
##this can take some time
#tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
#tfs = tfidf.fit_transform(token_dict.values())

#jaccard method
def jaccard_similarity(s1, s2):
	def add_space(s):
		return ' '.join(list(s))

	# 将字中间加入空格
	s1, s2 = add_space(s1), add_space(s2)
	# 转化为TF矩阵
	cv = CountVectorizer(tokenizer=lambda s: s.split())
	corpus = [s1, s2]
	vectors = cv.fit_transform(corpus).toarray()
	# 求交集
	numerator = np.sum(np.min(vectors, axis=0))
	# 求并集
	denominator = np.sum(np.max(vectors, axis=0))
	# 计算杰卡德系数
	return 1.0 * numerator / denominator

#tfidf method
def tfidf_similarity(s1, s2):
	def add_space(s):
		return ' '.join(list(s))

	# 将字中间加入空格
	s1, s2 = add_space(s1), add_space(s2)
	# 转化为TF矩阵
	cv = TfidfVectorizer(tokenizer=lambda s: s.split())
	corpus = [s1, s2]
	vectors = cv.fit_transform(corpus).toarray()
	# 计算TF系数
	return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))
	
# tf method	
def tf_similarity(s1, s2):
	def add_space(s):
		return ' '.join(list(s))

	# 将字中间加入空格
	s1, s2 = add_space(s1), add_space(s2)
	# 转化为TF矩阵
	cv = CountVectorizer(tokenizer=lambda s: s.split())
	corpus = [s1, s2]
	vectors = cv.fit_transform(corpus).toarray()
	# 计算TF系数
	return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))


#s1 = '赌博代购澳门新葡京'
#s2 = '澳门新葡京线上赌博欢迎你'
#print(jaccard_similarity(s1, s2))

s1="微信，奢侈品，赌博，代购，澳门，百家乐，新葡京，贷款，利息，收益,娱乐城，福利，美女，包包，在线发牌，，游戏，提款"
#text = open("list.txt")
#line = text.read()
file_n = 0
file_name = 'extracted_text_'

test = open("list.txt")
temp = []

#read file list


while True:
	line = test.readline()
	print(line)
	temp.append(line)
#	print(line)
	if not line: 
		break
		
test.close()
print(temp)

length = len(temp)
print(temp)
final = 0

for i in range(length-1):
	name = file_name+str(file_n)+'.txt'
	f = open(name)
	text = f.read()
	result = jaccard_similarity(s1, text)
	if result > 0.1:
		final +=1
	print(jaccard_similarity(s1, text))
	
print("pecent: ", final/(length -1))




	

#text = open("list1.txt")
#line1 = text.read()

#print(jaccard_similarity(line, line1))
