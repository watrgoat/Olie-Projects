# main.py

from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# draws a scatter plot such that each cluster's points are in different colors
def draw_clustered_graph(k, X, clusters, centroids):
  colors = ['r', 'g', 'b', 'y', 'c', 'm']
  fig, ax = plt.subplots()
  for i in range(k):
    points = []
    for j in range(len(X)):
      if clusters[j] == i:
        points.append(X[j])
    points = np.array(points)
    ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
  ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='#050505')
  plt.savefig("clustered_graph.png")


# release date, total gross
data = pd.read_csv("disney_movies.csv")
gross = data["inflation_adjusted_gross"]
raw_dates = data["release_date"]
years = []
edit_years = []
edit_gross = []

for date in raw_dates:
  dash_index = date.index('-')
  years.append(int(date[:dash_index]))
  for i in range(len(years)):
    if years[i] > 1980:
      edit_years += [years[i]]
      edit_gross += [gross[i]]


plt.scatter(edit_years, edit_gross, 7)
plt.savefig("precluster.png")
plt.clf()

k = 4
X = list(zip(edit_years, edit_gross))

km = KMeans(
  n_clusters=k, init='random',
  n_init=10, max_iter=300,
  tol=1e-04, random_state=0
)

clusters = km.fit_predict(X)
centroids = km.fit(X).cluster_centers_

# graph after clustering
draw_clustered_graph(k, X, clusters, centroids)
