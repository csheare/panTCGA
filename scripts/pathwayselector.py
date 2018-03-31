'''

pathwayselector.py

        This script allows you to select a signaling pathway (by name from hallmark_experiments.txt(*sensative*)) and recieve a submatrix from the
        matrix specified

        The program expects a directory path that contains the following formated files:

        pathway : <pathway name>
        output  : <output file name *must be numpy array>

        Important File Placements:
            These should be in data folder:
                ensembles_to_hallmark_id.json
                gene_dict.json
                hallmark_experiments.txt
                hallmark_gene_counts.json

                <below data is in drive>
                sample_class_list.txt
                panTCGA_float_data.npy
                gene_list_panTCGA.npy
                panTCGA_tumor_count_v1.json

example use:  python pathwayselector.py --pathway "HALLMARK_DNA_REPAIR" --output dna_repair.npy

'''
# returns an array of the RNAseq values across all samples for a gene
# gene must be in ensemble format
def getGeneSamples(gene):
    print("find Genes")

# returns a list of genes in ensemble format
# gene_list is a list of genes in hallmark format
def convertGenes(gene_list):
    print("convert Genes")

#returns a array of the genes in the pathway in ensemble format
def getPathwayGenes(pathway):

#write an array to ofile that is the specified pathway submatrix
def getSubMatrix(pathway,ofile):



if __name__ == '__main__':

        parser = argparse.ArgumentParser(description='Get Specific Pathway Matrix')
        parser.add_argument('--pathway', help='pathway name', type=str, required=True)
        parser.add_argument('--output', help='output file name', type=str, required=True)

        args = parser.parse_args()

        getSubMatric(args.pathway,args.output)
