import csv
import sys

def getComponentandKval(csv_f,pathway):

    with open(csv_f) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[0] == pathway:
                    pc = row[1]
                    kv = row[2]
                    return (pc,kv)
                    #print("Number of Principle Components: " + pc + "\n" + "Best K-Value: " + kv)



getComponentandKval("../data/final.csv","HALLMARK_DNA_REPAIR")
