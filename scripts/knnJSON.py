import os
import sys

newFile = open("Names.txt", "w")

for file in os.listdir("../data/pathways"):
    if file.endswith(".json"):
        filename = str(file)
        filename = filename[0:(len(filename) - 5)]
        newFile.write(filename + "\n")
        os.system('python ../models/knn.py --data "' + str(file) + '" --output "../graphs/' + str(filename) + '.png"')

newFile.close()
