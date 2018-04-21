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

# data = json.load(open("../data/pathways"))

# for key in data.keys():
# 	if not os.path.exists("../data/pathways/" + str(key) + '.json'):
# 		print(key)
# 		os.system('python pathwayselector.py --pathway "' + str(key) + '" --output "' + str(key) + '.json"')
#
#
# 		python knn.py --data "HALLMARK_BILE_ACID_METABOLISM.json" --output "hallmark_bi
# le_acid_metabolism.png"
