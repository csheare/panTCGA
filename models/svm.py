import pandas as pd
import numpy as np
import json
import os
import sys, argparse

from sklearn.metrics import accuracy_score
from genes_sample_swap import swap_axis, add_sample_labels
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.decomposition import PCA

'''
        The program converts the json to appropriate form via the functions in genes_sample_swap,
        Then it performs SVM

        example use:  python svm.py --data "dna_repair.json"

        #TODO: try with PCA


'''

def svm_classify(matrix,comp):

    #Data Prep
    full_data = pd.DataFrame(matrix)
    full_data = full_data.rename(columns={matrix.shape[1]-1: "TARGET CLASS"})

    #Scale the Datas
    scaler = StandardScaler()
    scaler.fit(full_data.drop("TARGET CLASS", axis=1))
    scaled_features = scaler.transform(full_data.drop("TARGET CLASS", axis=1))
    df_feat = pd.DataFrame(scaled_features,columns=full_data.columns[:-1])

    X=df_feat
    y= full_data["TARGET CLASS"]

    #Split the Data
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2)

    #Create Model
    print("Making Model...")
    model = svm.SVC(kernel="linear", C=1, gamma=1)

    #pca
    pca = PCA(n_components=int(comp))
    print("PCA...")
    pca_result_x_train = pca.fit_transform(X_train)
    pca_result_x_test = pca.transform(X_test)

    # #Fit Model
    print("Fitting...")
    model.fit(pca_result_x_train,y_train)
    print("Prediction...")
    pred = model.predict(pca_result_x_test)

    # #Train Model

    # print("Fitting Model...")
    # model.fit(X_train, y_train)
    # #
    # # #Predict Output
    # print("Predicting Model...")
    # pred= model.predict(X_test)
    print(accuracy_score(pred,y_test.tolist()))



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get Specific Pathway Matrix')
    parser.add_argument('--data', help='data file name', type=str, required=True)
    parser.add_argument('--comp', help='data file name', type=int, required=True)

    args = parser.parse_args()

    print("Processing ..." + str(args.data))
    matrix_with_labels = add_sample_labels(swap_axis(args.data))
    svm_classify(matrix_with_labels,args.comp)
