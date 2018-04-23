'''

processClassifers.py

        This script allows you to find the appropriate K value for KNN or SVM and the
        Component for PCA
'''

import os
import sys, argparse
import csv

def getComponentandKval(csv_f,pathway):

    with open(csv_f) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[0] == pathway:
                    pc = row[1]
                    kv = row[2]
                    return (pc,kv)
                    #print("Number of Principle Components: " + pc + "\n" + "Best K-Value: " + kv)

def runAllKNN():
    newFile = open("Names.txt", "w")

    for file in os.listdir("../data/pathways"):
        if file.endswith(".json"):
            filename = str(file)
            filename = filename[0:(len(filename) - 5)]#get just the file Name
            newFile.write(filename + "\n")
            CK_tuple = getComponentandKval("../data/final.csv",filename)
            os.system('python ../models/knn.py --data ' + str(file) + ' --K  '  + str(CK_tuple[1]) + ' --Component ' + str(CK_tuple[0]))
    newFile.close()

def runAllSVM():
    newFile = open("Names.txt", "w")

    for file in os.listdir("../data/pathways"):
        if file.endswith(".json"):
            filename = str(file)
            filename = filename[0:(len(filename) - 5)]
            newFile.write(filename + "\n")
            CK_tuple = getComponentandKval("../data/final.csv",filename)
            os.system('python ../models/svm.py --data ' + str(file) + ' --Component ' + str(CK_tuple[0]))

    newFile.close()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get Specific Pathway Matrix')
    parser.add_argument('--classifier', help='svm or knn', type=str, required=True)

    args = parser.parse_args()

    if args.classifier == "KNN":
        runAllKNN()
    if args.classifier == "SVM":
        runAllSVM()
