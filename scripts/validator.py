import numpy as np
import json
import os
import sys, argparse

'''
validator.py

	This script compares the number of rows in the submatrix to the actual number of genes in the subset

	example input: python validator.py --pathway "HALLMARK_DNA_REPAIR" --output "dna_repair.json"
	example output: Genes in:

		HALLMARK_DNA_REPAIR is 150
		Len of Output File:150
		True

'''

def isValid(pathway, output):
	#Grab the  Pathway from the hallmark file
	with open("../data/hallmark_gene_counts.json",'r') as f:
		gene_counts = json.load(f)

	count = gene_counts[pathway]
	print("Genes in: "+ str(pathway) +" is " +str(count))

	#Get the line length of the file
	with open("../data/pathways/"+output,'r') as f:
		output = json.load(f)
	print("Len of Output File:" + str(len(output)))
	return len(output) == count



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get Specific Pathway Matrix')
    parser.add_argument('--pathway', help='pathway name', type=str, required=True)
    parser.add_argument('--output', help='output file name', type=str, required=True)

    args = parser.parse_args()

    print(isValid(args.pathway,args.output))
