import csv
import sys

with open('examplesheet.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        for field in row:
            if field == sys.argv[1]:
                pc = row[1]
                kv = row[2]
                print("Number of Principle Components: " + pc + "\n" + "Best K-Value: " + kv)
