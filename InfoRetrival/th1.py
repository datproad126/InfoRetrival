
docs_has_been_tokenization = {
	'approach': [0,0,1,0],
	'breakthrough': [1,0,0,0],
	'drug': [1,1,0,0],
	'for': [1,0,1,1],
	'hopes': [0,0,0,1],
	'new': [0,1,1,1],
	'of': [0,0,1,0],
	'patients': [0,0,0,1],
	'schizophrenia': [1,1,1,1],
	'treatment': [0,0,1,0]
}
docs_has_been_tokenization_number = {
	'approach': [3],
	'breakthrough': [1],
	'drug': [1,2],
	'for': [1,3,4],
	'hopes': [4],
	'new': [2,3,4],
	'of': [3],
	'patients': [4],
	'schizophrenia': [1,2,3,4],
	'treatment': [3]
}
class TH1:
	def __init__(self, docID):
		self.docID = docID

	def Intersect(self, p1, p2):
		 return [value for value in self.docID.get(p1) if value in self.docID.get(p2)]

	def Union(self, p1, p2):
		answers = []
		for value in self.docID.get(p1):
			if value in self.docID.get(p2) or value not in self.docID.get(p2): answers.append(value)
		for value in self.docID.get(p2):
			if value not in answers: answers.append(value)
		return answers

	def Intersect_with_Disjunction(self, p1, p2):
		return [value for value in self.docID.get(p1) if value not in self.Intersect(p1, p2)]

print(TH1(docs_has_been_tokenization_number).Intersect_with_Disjunction('for','new'))
