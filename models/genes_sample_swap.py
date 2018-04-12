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

#This function will swap the axis and return the new dictionary
# Step 1
def swap_axis(old_file):
    with open("../data/pathways/"+str(old_file),'r') as f:
        old_dict = json.load(f)

    old_matrix = np.array([old_dict[i] for i in old_dict.keys()])

    new_matrix = np.transpose(old_matrix)

    return new_matrix

#Step 2
def add_sample_labels(new_matrix):
    temp = open("../data/sample_class_list.txt","r")
    temp = temp.readlines()

    for i in range(len(temp)):
        temp[i] = temp[i].split("\t")[1]
        temp[i] = temp[i].replace("\n","")

    array = np.asarray(temp)

    matrix_with_labels = np.column_stack((new_matrix,array))

    return matrix_with_labels



# if __name__ == '__main__':
#
#     parser = argparse.ArgumentParser(description='Get Specific Pathway Matrix')
#     parser.add_argument('--old_file', help='pathway name', type=str, required=True)
#     parser.add_argument('--new_file', help='output file name', type=str, required=True)
#
#     args = parser.parse_args()
#
#     matrix_with_labels = addSampleLabels(swapAxis(args.old_file))
#
#     outputFile = open("../data/cleaned/"+ str(args.new_file),"wb")
#     np.save(outputFile,matrix_with_labels);
