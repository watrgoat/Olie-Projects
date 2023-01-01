import pandas as pd
import tensorflow
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

filepath = 'https://static.junilearning.com/ai_level_2/diabetes.csv'
# dataset: https://www.kaggle.com/uciml/pima-indians-diabetes-database
# read in data and split into feature vectors and classifications
data = pd.read_csv(filepath)
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# X.head()
# y.head()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=1)

model = Sequential()
model.add(Dense(20, input_dim=8, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=300, validation_split=0.2, batch_size=10)

model.evaluate(X_test, y_test)
