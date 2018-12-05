# Python program to demonstrate # KNN classification algorithm # on IRISdataset
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris_dataset=load_iris()

print("\n IRIS FEATURES TARGET NAMES: \n ", iris_dataset.target_names)
X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0)

kn = KNeighborsClassifier(n_neighbors=2,metric='minkowski',p=2)
kn.fit(X_train,y_train)
prediction = kn.predict(X_test)
print("predicted",prediction)
print("actual",y_test)
print("accuracy_score",accuracy_score(y_test,prediction))