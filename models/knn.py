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
from genes_sample_swap import swap_axis, add_sample_labels,swap_the_big_ol_matrix,get_the_big_ol_matrix

'''
        The program converts the json to appropriate form via the functions in genes_sample_swap,
        Then it performs PCA and KNN on the data


        example use:  python knn.py --data "dna_repair.json"


'''
import csv

# TODO:


def knn_classify(matrix,k_val,component_val,output):
    full_data = pd.DataFrame(matrix)
    full_data = full_data.rename(columns={matrix.shape[1]-1: "TARGET CLASS"})

    #Scale the Datas
    scaler = StandardScaler()
    scaler.fit(full_data.drop("TARGET CLASS", axis=1))
    scaled_features = scaler.transform(full_data.drop("TARGET CLASS", axis=1))
    df_feat = pd.DataFrame(scaled_features,columns=full_data.columns[:-1])

    X=df_feat
    y= full_data["TARGET CLASS"]


    #Train the Model
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2)


    #Principle Component Analysis
    # pca = PCA(n_components=int(component_val))
    # pca_result_x_train = pca.fit_transform(X_train)
    # pca_result_x_test = pca.transform(X_test)

    #Use this to Find Optimal Number of Components (components by varaince)
    pca = PCA(n_components=(X.shape)[1])
    pca_result_x_train = pca.fit_transform(X_train)

    plt.figure(figsize=(10,6))
    plt.plot(range(0,50),pca.explained_variance_[:50], color='blue',linestyle='dashed', marker='o', markerfacecolor='red', markersize=4)
    plt.title("Full Data Component Analysis")
    plt.xlabel("Number of Components")
    plt.ylabel("Variance")
    plt.savefig(output)

    #KNN
    # knn = KNeighborsClassifier(n_neighbors=int(k_val))
    # knn.fit(X_train,y_train)
    # pred = knn.predict(X_test)

    #Confusion Matrix
    #print(confusion_matrix(y_test,pred))

    #K folds cross validation
    #Use this to Find Optimal K Value
    # error_rate = []
    # for i in range(1,(X.shape)[1]+1):
    #     print("Num Neighbors is: " + str(i))
    #     knn = KNeighborsClassifier(n_neighbors=i)
    #     knn.fit(X_train,y_train)
    #     pred_i = knn.predict(X_test)
    #     error_rate.append(np.mean(pred_i != y_test))
    #
    # plt.figure(figsize=(10,6))
    # plt.plot(range(0,(X.shape)[1]),error_rate, color='blue',linestyle='dashed', marker='o', markerfacecolor='red', markersize=3)
    # plt.title("Error Rate v K Value")
    # plt.xlabel("K")
    # plt.ylabel("Error Rate")
    # plt.savefig(output)
    #
    # #Compute error_rate
    #
    print(accuracy_score(pred,y_test.tolist()))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get Specific Pathway Matrix')
    parser.add_argument('--data', help='data file name', type=str, required=True)
    parser.add_argument('--output', help='data file name', type=str, required=False)
    #parser.add_argument('--K', help='optimal K value', type=str, required=True)
    #parser.add_argument('--Component', help='optimal Component', type=str, required=True)

    args = parser.parse_args()
    print("Processing ..." + str(args.data))
    #matrix_with_labels = add_sample_labels(swap_axis(args.data))
    #knn_classify(matrix_with_labels,args.K,args.Component,args.output)
    knn_classify(swap_the_big_ol_matrix(),0,0,args.output)
