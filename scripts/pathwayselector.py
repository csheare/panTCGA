'''

pathwayselector.py

        This script allows you to select a signaling pathway (by name from hallmark_experiments.txt(*sensative*)) and recieve a submatrix from the
        matrix specified

        The program expects a directory path that contains the following formated files:

        pathway : <pathway name>
        output  : <output file name *must be numpy array>

        Important File Placements:
            These should be in data folder:
                filesforpathwayscript.tar <of course, un-tar it, it is still like 10GB :> >

example use:  python pathwayselector.py --pathway "HALLMARK_DNA_REPAIR" --output "dna_repair.json"

'''
import numpy as np
import json
import os
import sys, argparse

# returns an array of the RNAseq values across all samples for a gene
# gene must be in ensemble format
def getGeneSamples(gid,gene_list,matrix):
    if gid in gene_list.keys():
        gene_num = gene_list[str(gid)]
    else:
        return None
    return list(matrix[gene_num])

# returns a list of genes in ensemble format
# gene_list is a list of genes in hallmark format
# Note: if there is not a mapping, google "ensemble id for 'KeyError: ' '", and add it to hallmark_id_to_ensembles.json, kinda lame srry
def convertGenes(gene_list):
    with open("../data/hallmark_id_to_ensembles.json", 'r') as f:
        conversion_dict = json.load(f)
    converted_genes = []
    for gene in gene_list:
        converted_genes.append(conversion_dict[gene])
    return converted_genes

#returns a list of the genes in the pathway in ensemble format
# step 1
def getPathwayGenes(pathway):
    with open("../data/gene_dict.json", 'r') as f:
        gene_dict = json.load(f)
    gene_dict[pathway][-1] = gene_dict[pathway][-1].replace("'","")
    return gene_dict[pathway]


#write an array to ofile that is the specified pathway submatrix
def getSubMatrix(pathway,ofile):
    pathway_genes = getPathwayGenes(pathway)
    converted_genes = convertGenes(pathway_genes)

    with open("../data/gene_list_panTCGA.json", 'r') as f:
        gene_list = json.load(f)
    matrix = np.load("../data/panTCGA_gct_data_float_v1.npy")
    samples_per_gene = {}
    for possible_genes in converted_genes:
        for gid in possible_genes:
            samples_per_gene[gid] = getGeneSamples(gid,gene_list,matrix)
            if(samples_per_gene[gid] is None):
                del samples_per_gene[gid]
                continue
            else:
                break
    with open("../data/pathways/" + str(ofile), 'w') as f:
        json.dump(samples_per_gene,f)
    #write samples_per_gene to ofile


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get Specific Pathway Matrix')
    parser.add_argument('--pathway', help='pathway name', type=str, required=True)
    parser.add_argument('--output', help='output file name', type=str, required=True)

    args = parser.parse_args()

    getSubMatrix(args.pathway,args.output)
