import json
import os
import pathwayselector

data = json.load(open("../data/gene_dict.json"))

for key in data.keys():
	if not os.path.exists("../data/pathways/" + str(key) + '.json'):
		print(key)
		os.system('python pathwayselector.py --pathway "' + str(key) + '" --output "' + str(key) + '.json"')