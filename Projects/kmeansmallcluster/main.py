# main.py
from copy import deepcopy
import pandas as pd
import matplotlib.pyplot as plt
import random
import math


# draws a scatterplot such that each cluster's points are in different colors
def draw_clustered_graph(k, X, clusters, centroids):
    colors = ['r', 'g', 'b', 'y', 'c', 'm']
    fig, ax = plt.subplots()
    for i in range(k):
        xpoints = []
        ypoints = []
        for j in range(len(X)):
            if clusters[j] == i:
                xpoints.append(X[j][0])
                ypoints.append(X[j][1])
        ax.scatter(xpoints, ypoints, s=7, c=colors[i])
    xpoints = []
    ypoints = []
    for c in centroids:
        xpoints.append(c[0])
        ypoints.append(c[1])
    ax.scatter(xpoints, ypoints, marker='*', s=200, c='#050505')
    plt.savefig("clustered_graph.png")


def calc_dist(a, b):
    total = 0
    for i in range(len(a)):
        total += a[i] ** 2 + b[i] ** 2
    total = math.sqrt(total)
    return total
    # calculate distance between points (pythagorean theorem)


def centroid_calc(points):
    xsum = 0
    ysum = 0
    for values in points:
        xsum += values[0]
        ysum += values[1]
        return xsum / len(points), ysum / len(points)


# calculate centroid of a list of points

data = pd.read_csv("Mall_Customers.csv")
income = data["Annual Income (k$)"]
spending = data["Spending Score (1-100)"]
plt.scatter(income, spending, 7)
plt.savefig("pre-cluster.png")
plt.clf()

k = 5
X = list(zip(income, spending))

centroids = []
for i in range(k):
    rand_index = random.randint(0, len(X) - 1)
    x = X[rand_index][0]
    y = X[rand_index][1]
    centroids.append((x, y))

prev_centroids = []
for i in range(k):
    prev_centroids.append((0, 0))

clusters = [0] * len(X)
# makes list with X number of values of 0

while centroids != prev_centroids:
    for i in range(len(X)):
        min_dist = math.inf
        for z in range(k):
            distance = calc_dist(X[i], centroids[z])
            if distance < min_dist:
                min_dist = distance
                clusters[i] = z
        print(clusters)
    prev_centroids = deepcopy(centroids)

temp_points = []
for i in range(k):
    for j in range(0, len(clusters)):
        if i == clusters[j]:
            temp_points += [X[j]]
    centroids[i] = centroid_calc(temp_points)
    temp_points = []

print(centroids)
draw_clustered_graph(k, X, clusters, centroids)

# hw: finish calculating centroids
# generate clustered graph
# make new list of points
# make those points assigned to cluster
# centroids at i = calc_centroid(new point list)




