import pandas as pd
import numpy as np
import json
import os
import sys, argparse
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score
from genes_sample_swap import swap_axis, add_sample_labels,swap_the_big_ol_matrix,get_the_big_ol_matrix
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from mpl_toolkits.mplot3d import Axes3D
from sklearn.manifold import TSNE


def kmeans(matrix):


    full_data = pd.DataFrame(matrix)
    X = np.asarray(full_data)[:,:-1]

    #Perform PCA
    pca = TSNE(n_components=15)
    X = pca.fit_transform(X)

    # Number of clusters
    kmeans = KMeans(n_clusters=33)

    kmeans = kmeans.fit(X)

    print(X.shape)

    # Getting the cluster labels
    y_kmeans = kmeans.predict(X)

    # Centroid values
    centers = kmeans.cluster_centers_


    #print(centroids) # From sci-kit learn

    plt.rcParams['figure.figsize'] = (16, 9)

    # Creating a sample dataset with 4 clusters

    print(len(X[:, 0]))
    print(len(X[:, 1]))
    print(y_kmeans)

    fig = plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')


    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

    plt.show()



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get Specific Pathway Matrix')
    parser.add_argument('--data', help='data file name', type=str, required=False)

    args = parser.parse_args()

    kmeans(swap_the_big_ol_matrix())
    #kmeans(get_the_big_ol_matrix())
    #matrix_with_labels = add_sample_labels(swap_axis(args.data))
    #kmeans(matrix_with_labels)
