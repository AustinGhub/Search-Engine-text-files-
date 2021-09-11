#Contributors: Austin Truong and Austin Tran

####################################################################################
from pathlib import Path
import re, csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
####################################################################################

def fileAnalysis(queryWord):
	count = 0
	all_docs = list()
	documents = list()
	pathDirectory = (Path(".")/"large-sample").glob('*.txt')
	for file in pathDirectory:
		documents.append(file.name)
		# if count != 7:
		with open(file, 'r', encoding='utf-8') as currentFile:
			fileString = currentFile.read()
			fileString = re.sub(r'[^a-zA-Z]', ' ', fileString)
			fileString = re.sub(r'\s{2,}', ' ', fileString)
			fileString = re.sub(r'[0-9]', '', fileString)
			all_docs.append(fileString)
			count += 1

	#Builds the TFIDF Matrix
	vectorizer = TfidfVectorizer()
	vectors = vectorizer.fit_transform(all_docs)
	search_query_weights = vectorizer.transform([queryWord])

	#Does the cosine similarity
	cosine_distance = cosine_similarity(search_query_weights, vectors)
	similarity_list = cosine_distance[0]

	return similarity_list, documents

def most_similar(similarity_list, min_talks=1):
	#Picks the txt files with the highest similarity values
	most_similar= []
  
	while min_talks > 0:
		tmp_index = np.argmax(similarity_list)
		most_similar.append(tmp_index)
		similarity_list[tmp_index] = 0
		min_talks -= 1

	return most_similar

class QuerySearch:
	def __init__(self):
		self.TFIDF_values = list()
		self.tfidfList = list()
		self.docList = list()
		self.relaventDocNames = list()

		self.searchResults = list()

	def corpusSearch(self, query):
		self.tfidfList, self.docList = fileAnalysis(query)

		for value in self.tfidfList:
			self.TFIDF_values.append(value)

		self.relaventDocNames = most_similar(self.tfidfList, 5) 

		self.searchResults = [(round(self.TFIDF_values[index],5), self.docList[index]) for index in self.relaventDocNames]
		return self.searchResults

	def printResults(self):
		for value,fileName in self.searchResults:
			print(value," - ",fileName)

	