import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([10, 8, 7.5, 7, 6, 6, 7, 9, 8.5, 11])

plt.scatter(x, y, s=50)
plt.savefig("before.png")
plt.clf()

model = LinearRegression()

model.fit(x, y)
corr = model.score(x, y)
b = model.intercept_
m = model.coef_[0]

print(corr)
print(b)
print(m)

plt.scatter(x, y, s=50)
plt.plot(x, x*m+b, 'r')
plt.savefig("after.png")
plt.clf()
