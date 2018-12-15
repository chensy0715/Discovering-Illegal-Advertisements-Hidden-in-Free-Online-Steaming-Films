from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy.linalg import norm
import time

#https://juejin.im/post/5b237b45f265da59a90c11d6

#using different ways to test time comsuption and accuracy for Enlighs and Chinese

#for English
print("##############testing English###############")

#TF method
start = time.clock()
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

s1 = 'you are an good people and friendly'
s2 = 'you are an bad guy, '

s3 = "There is several ways to complete this lab task. In common, we can use either ZAP intercept tool or Firefox developing tool to finish this task."
s4 = "we can use directly ZAP tool to directly break the process after the click and intercept the Post Request. We can directly change the value to"

print("tf method:")

print("similarity accuracty:", tf_similarity(s1, s2))

print("similarity accuracty:", tf_similarity(s3, s4))
print("similarity accuracty:", tf_similarity(s3, s1))
end = time.clock()
print("time:", end -start)

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.linalg import norm

#TFIDF
start = time.clock()
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

s1 = 'you are an good people and friendly'
s2 = 'you are an bad guy, '


s3 = "There is several ways to complete this lab task. In common, we can use either ZAP intercept tool or Firefox developing tool to finish this task."
s4 = "we can use directly ZAP tool to directly break the process after the click and intercept the Post Request. We can directly change the value to"

print("tfidf method")
print("similarity accuracty", tfidf_similarity(s1, s2))
print("similarity accuracty", tfidf_similarity(s3, s4))
print("similarity accuracty", tfidf_similarity(s3, s1))


end = time.clock()
print("time:", end -start)


#Jaccard method

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy.linalg import norm


start = time.clock()

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

s1 = 'you are an good people and friendly'
s2 = 'you are an bad guy, '

s3 = "There is several ways to complete this lab task. In common, we can use either ZAP intercept tool or Firefox developing tool to finish this task."
s4 = "we can use directly ZAP tool to directly break the process after the click and intercept the Post Request. We can directly change the value to"

print("jaccard method")
print("similarity accuracty",jaccard_similarity(s1, s2))
print("similarity accuracty",jaccard_similarity(s3, s4))
print("similarity accuracty",jaccard_similarity(s3, s1))

end = time.clock()
print("time:", end -start)







################################################################################################
#for Chinese:
print("##############testing Chinese###############")


from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy.linalg import norm
import time

#https://juejin.im/post/5b237b45f265da59a90c11d6

#using different ways to test time comsuption and accuracy

#TF method
start = time.clock()
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

s1 = '你在干嘛呢'
s2 = '你在干什么呢'

s3 = '赌博代购微信奢侈品贷款收益澳门新葡京百家乐福利美女'
s4 = '澳门新葡京娱乐场线上百家乐赌博欢迎你，在线发牌看福利美女奢侈品牌，高品质，代购，全球包包'
s5 = '看福利美女'
s6 = '奢侈品牌，高品质，代购，全球包包'
print("tf method")
#print("similarity accuracty 1 and 2:", tf_similarity(s1, s2))
print("similarity accuracty 3 and 4:", tf_similarity(s3, s4))
print("similarity accuracty 3 and 4:", tf_similarity(s3, s4))
print("similarity accuracty 3 and 4:", tf_similarity(s3, s4))
print("similarity accuracty 3 and 4:", tf_similarity(s3, s4))
print("similarity accuracty 3 and 4:", tf_similarity(s3, s4))
print("similarity accuracty 3 and 4:", tf_similarity(s3, s4))
print("similarity accuracty 3 and 4:", tf_similarity(s3, s4))
print("similarity accuracty 3 and 4:", tf_similarity(s3, s4))
print("similarity accuracty 3 and 4:", tf_similarity(s3, s4))
print("similarity accuracty 3 and 4:", tf_similarity(s3, s4))

#print("similarity accuracty 3 and 5:", tf_similarity(s3, s5))
#print("similarity accuracty 3 and 6:", tf_similarity(s3, s6))
#print("similarity accuracty 3 and 6:", tf_similarity(s3, s1))
end = time.clock()
print("time:", end -start)

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.linalg import norm

#TFIDF
start = time.clock()
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

s1 = '你在干嘛呢'
s2 = '你在干什么呢'
s3 = '赌博代购微信奢侈品贷款收益澳门新葡京百家乐福利美女'
s4 = '澳门新葡京娱乐场线上百家乐赌博欢迎你，在线发牌看福利美女奢侈品牌，高品质，代购，全球包包'
s5 = '看福利美女'
s6 = '奢侈品牌，高品质，代购，全球包包'

print("tfidf method")
#print("similarity accuracty 1 and 2", tfidf_similarity(s1, s2))
print("similarity accuracty 3 and 4", tfidf_similarity(s3, s4))
print("similarity accuracty 3 and 4", tfidf_similarity(s3, s4))
print("similarity accuracty 3 and 4", tfidf_similarity(s3, s4))
print("similarity accuracty 3 and 4", tfidf_similarity(s3, s4))
print("similarity accuracty 3 and 4", tfidf_similarity(s3, s4))
print("similarity accuracty 3 and 4", tfidf_similarity(s3, s4))
print("similarity accuracty 3 and 4", tfidf_similarity(s3, s4))
print("similarity accuracty 3 and 4", tfidf_similarity(s3, s4))
print("similarity accuracty 3 and 4", tfidf_similarity(s3, s4))
print("similarity accuracty 3 and 4", tfidf_similarity(s3, s4))
#print("similarity accuracty 3 and 5", tfidf_similarity(s3, s5))
#print("similarity accuracty 3 and 6", tfidf_similarity(s3, s6))
#print("similarity accuracty", tfidf_similarity(s3, s1))

end = time.clock()
print("time:", end -start)


#Jaccard method

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy.linalg import norm


start = time.clock()

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

s1 = '你在干嘛呢'
s2 = '你在干什么呢'
s3 = '赌博代购微信奢侈品贷款收益澳门新葡京百家乐福利美女'
s4 = '澳门新葡京娱乐场线上百家乐赌博欢迎你，在线发牌看福利美女奢侈品牌，高品质，代购，全球包包'
s5 = '看福利美女'
s6 = '奢侈品牌，高品质，代购，全球包包'

print("jaccard_similartiy")

#print("similarity accuracty 1 and 2",jaccard_similarity(s1, s2))
print("similarity accuracty 3 and 4",jaccard_similarity(s3, s4))
print("similarity accuracty 3 and 4",jaccard_similarity(s3, s4))
print("similarity accuracty 3 and 4",jaccard_similarity(s3, s4))
print("similarity accuracty 3 and 4",jaccard_similarity(s3, s4))
print("similarity accuracty 3 and 4",jaccard_similarity(s3, s4))
print("similarity accuracty 3 and 4",jaccard_similarity(s3, s4))
print("similarity accuracty 3 and 4",jaccard_similarity(s3, s4))
print("similarity accuracty 3 and 4",jaccard_similarity(s3, s4))
print("similarity accuracty 3 and 4",jaccard_similarity(s3, s4))
print("similarity accuracty 3 and 4",jaccard_similarity(s3, s4))
#print("similarity accuracty 3 and 5", jaccard_similarity(s3, s5))
#print("similarity accuracty 3 and 6", jaccard_similarity(s3, s6))
#print("similarity accuracty 3 and 7", jaccard_similarity(s3, s1))
end = time.clock()
print("time:", end -start)
