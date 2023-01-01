from copy import deepcopy
import pandas as pd
import matplotlib.pyplot as plt
import random
import math


def calculate_dist(a, b):
    total = 0
    for i in range(len(a)):
        total += (a[i] - b[i]) ** 2
    return total ** 0.5


def is_same(a, b):
    for i in range(len(a)):
        if a != b:
            return False
    return True


def calculate_centroid(points):
    x_sum = 0
    y_sum = 0
    for point in points:
        x_sum += point[0]
        y_sum += point[1]
    return (x_sum / len(points), y_sum / len(points))


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
        print("Cluster Number: " + str(i) + " | Color: " + colors[i])

    xpoints = []
    ypoints = []
    for c in centroids:
        xpoints.append(c[0])
        ypoints.append(c[1])
    ax.scatter(xpoints, ypoints, marker='*', s=200, c='#050505')
    plt.savefig("clustered_graph.png")
    print()


# read in the data
data = pd.read_csv('customers.csv')
income = data['Annual Income']
spending = data['Spending Score']

# graph before any clustering
plt.scatter(income, spending, s=7)
plt.savefig("before_clustering.png")
plt.clf()

k = 5
# builds array of data points
X = list(zip(income, spending))

# initialize random centroids
centroids = []

for i in range(k):
    random_index = random.randint(0, len(income) - 1)
    x = X[random_index][0]
    y = X[random_index][1]
    centroids.append((x, y))

# build array of tuples to store old centroids
old_centroids = []
for i in range(k):
    old_centroids.append((0, 0))

# index i in clusters stores the cluster assigned for data point i
clusters = [0] * len(X)

# if error is 0 then the centroids have not moved from the last iteration (therefore we can stop)
while not is_same(centroids, old_centroids):
    # calculate distance from each centroid for each data point
    for i in range(len(X)):
        min_dist = math.inf
        for j in range(len(centroids)):
            dist = calculate_dist(X[i], centroids[j])
            if dist < min_dist:
                min_dist = dist
                clusters[i] = j

    # replace old centroids with current ones
    old_centroids = deepcopy(centroids)

    # calculate new centroids
    for i in range(k):
        points = []
        for j in range(len(X)):
            if clusters[j] == i:
                points.append(X[j])
        centroids[i] = calculate_centroid(points)

draw_clustered_graph(k, X, clusters, centroids)


def k_nearest_neighbor(k_near, X, clusters, new_point):
    nearest_dict = {}

    for point in X:
        distance = calculate_dist(point, new_point)
        if len(nearest_dict) < k_near:
            nearest_dict[point] = distance
        else:
            max_dist = -1
            max_point = (-1, -1)
            for dict_point in nearest_dict:
                if nearest_dict[dict_point] > max_dist:
                    max_dist = nearest_dict[dict_point]
                    max_point = dict_point
            if distance < max_dist:
                nearest_dict.pop(max_point)
                nearest_dict[point] = distance
    point_loc = []
    for point in nearest_dict:
        point_loc += [clusters[X.index(point)]]
    counter = 0
    num = point_loc[0]

    for m in point_loc:
        curr_frequency = point_loc.count(m)
        if curr_frequency > counter:
            counter = curr_frequency
            num = m
    return num


new_point = (100, 20)
k_near = 3
print(k_nearest_neighbor(k_near, X, clusters, new_point))
# test with points

# clusters for k nearest point and majority test
