'''

genes_sample_swap.py

        This file has functions that allow you to swap the x and y data values and add the labels in a additional
        column for the samples


        before:         Sample 1 | Sample 2 | Sample 3 ....
                GeneA  |  ##           ##       ##
                GeneB  |  ##           ##       ##
                GeneC  |  ##           ##       ##

        after:            GeneA | GeneB | GeneC .... | SampleLabel(Cancer Type)
                Sample1  |  ##     ##       ##          ACA
                Sample2  |  ##     ##       ##          ACA
                Sample3  |  ##     ##       ##          ACA

'''

import numpy as np
import json
import sys, argparse
import collections
import csv

#This function will swap the axis and return the new dictionary
def swap_axis(old_file):
    with open("../data/pathways/"+str(old_file),'r') as f:
        old_dict = json.load(f)

    old_matrix = np.array([old_dict[i] for i in old_dict.keys()])

    new_matrix = old_matrix.T

    return new_matrix


def add_sample_labels(new_matrix):
    temp = open("../data/sample_class_list.txt","r")
    temp = temp.readlines()

    for i in range(len(temp)):
        temp[i] = temp[i].split("\t")[1]
        temp[i] = temp[i].replace("\n","")

    array = np.asarray(temp)

    matrix_with_labels = np.column_stack((new_matrix,sorted(array)))

    return matrix_with_labels
