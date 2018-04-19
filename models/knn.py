import pandas as pd
import numpy as np
import json
import os
import sys, argparse
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix
from genes_sample_swap import swap_axis, add_sample_labels
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA


'''
        The program converts the json to appropriate form via the functions in genes_sample_swap,
        Then it performs PCA and KNN on the data


        example use:  python knn.py --data "dna_repair.json"


'''
import csv

# TODO:

#knn = KNeighborsClassifier())

def knn_classify(matrix):
    full_data = pd.DataFrame(matrix)
    full_data = full_data.rename(columns={matrix.shape[1]-1: "TARGET CLASS"})
    print(full_data.shape)

    X = np.asarray(full_data)[:,:-1]
    print(X.shape)
    y = np.asarray(full_data["TARGET CLASS"])

    print(X.shape)
    print(y.shape)

    print(X)

    #Train the Model
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2)


    #Principle Component Analysis
    pca = PCA(n_components=6)
    pca_result_x_train = pca.fit_transform(X_train)
    pca_result_x_test = pca.transform(X_test)#

    plt.scatter(pca_result_x_train[:, 0], pca_result_x_train[:, 1], edgecolor='none', alpha=0.5)
    plt.show()

    #plt.scatter(pca_result_x_train[:4000, 0], pca_result_x_train[:4000, 1])#, c=y_train[:4000], edgecolor='none', alpha=0.5,
    # #        cmap=plt.get_cmap('jet', 10), s=5)
    # # plt.colorbar()
    #plt.show()

    #KNN
    knn = KNeighborsClassifier(n_neighbors=20)
    knn.fit(X_train,y_train)
    pred = knn.predict(X_test)
    #print(confusion_matrix(y_test,pred))
    #print(classification_report(y_test,pred))

    # for i in range(len(pred)):
    #     print(str(pred[i]) + " : " + str(y_test.tolist()[i]))
    #print(pred)
    #print(y_test.tolist())
    #print(knn.score(pred,y_test.tolist()))


    #K folds cross validation
    #Use this to Find Optimal K Value
    #error_rate = []
    # for i in range(1,10):
    #
    #     knn =KNeighborsClassifier(n_neighbors=i)
    #     knn.fit(X_train,y_train)
    #     pred_i = knn.predict(X_test)
    #     error_rate.append(np.mean(pred_i != y_test))
    #
    # plt.figure(figsize=(10,6))
    # plt.plot(range(1,10),error_rate, color='blue',linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)
    # plt.title("Error Rate v K Value")
    # plt.xlabel("K")
    # plt.ylabel("Error Rate")
    #plt.show()

    #Compute error_rate

    print(accuracy_score(pred,y_test.tolist()))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get Specific Pathway Matrix')
    parser.add_argument('--data', help='data file name', type=str, required=True)

    args = parser.parse_args()

    matrix_with_labels = add_sample_labels(swap_axis(args.data))
    knn_classify(matrix_with_labels)
