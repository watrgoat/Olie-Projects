import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

data = pd.read_csv("iris.csv")
X = data.drop("species", axis=1)
y = data["species"]
custom_vectors = [[5.2, 3.1, 1.6, 0.3],[6.0, 3.0, 4.8, 1.1],[7.5, 3.0, 6.2, 2.0]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=4)

model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(model.predict(custom_vectors))
print(accuracy_score(y_test, y_pred))
