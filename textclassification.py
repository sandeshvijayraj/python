import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_20newsgroups

data=fetch_20newsgroups()
print()
print(list(data.target_names))
print()
categorie=['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware']
train = fetch_20newsgroups(subset='train',categories=categorie)
test = fetch_20newsgroups(subset='test',categories=categorie)

print('training data:',len(train.data))
print("testing data",len(test.data))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

model = make_pipeline(TfidfVectorizer(),MultinomialNB())
model.fit(train.data,train.target)

labels = model.predict(test.data)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(test.target,labels))

#lets predict now

def predict_category(s,train=train,model=model):
	pred = model.predict([s])
	return train.target_names[pred[0]]
while True:
	x=input()
	if(x=='0'):
		break
	print(predict_category(x))