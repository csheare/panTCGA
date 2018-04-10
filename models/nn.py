import pandas as pd
import numpy as np
import json
import os
import sys, argparse
#from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix
from genes_sample_swap import swap_axis, add_sample_labels


'''
        The program expects a directory path that contains the following formated files:

        pathway : <pathway name>
        output  : <output file name *must be numpy array>

        Note: This is to prepare the data for two types of analysis: clustering and classification

        example use:  python nn.py --data "dna_repair.json"


'''

# TODO:

#knn = KNeighborsClassifier())

def knn_classify(matrix):
    knn = KNeighborsClassifier()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get Specific Pathway Matrix')
    parser.add_argument('--data', help='data file name', type=str, required=True)

    args = parser.parse_args()

    matrix_with_labels = add_sample_labels(swap_axis(args.data))
    print(matrix_with_labels)
