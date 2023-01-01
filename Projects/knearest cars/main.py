import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Dataset: https://sci2s.ugr.es/keel/dataset.php?cod=56#sub2

# read in data and replace categories with dictionary values
data = pd.read_csv('cars.csv')

levels = {"vhigh": 3, "high": 2, "med": 1, "low": 0}
doors_dict = {"5more": 5, "4": 4, "3": 3, "2": 2}
persons_dict = {"2": 2, "4": 4, "more": 5}
lug_boot_dict = {"small": 0, "med": 1, "big": 2}
safety_dict = {"high": 1, "med": 2, "low": 3}
col_names = {"buying": levels, "maint": levels, "doors": doors_dict, "persons": persons_dict, "lug_boot": lug_boot_dict, "safety": safety_dict}

data.replace(col_names, inplace=True)
X = data.drop("acceptability", axis=1)
y = data["acceptability"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=100)

knn = KNeighborsClassifier(n_neighbors=1382)
knn.fit(X_train, y_train)
prediction = knn.predict([[1, 2, 4, 1, 1, ]])

print(accuracy_score(y_test, prediction))
# instanctiate and fit knearest neighbor
# make list of preditions from .predict functions