'''

genes_sample_swap.py

        This script allows swap the x and y data values and add the labels in a additional
        column for the samples


        before:         Sample 1 | Sample 2 | Sample 3 ....
                GeneA  |  ##           ##       ##
                GeneB  |  ##           ##       ##
                GeneC  |  ##           ##       ##

        after:            GeneA | GeneB | GeneC .... | SampleLabel(Cancer Type)
                Sample1  |  ##     ##       ##          ACA
                Sample2  |  ##     ##       ##          ACA
                Sample3  |  ##     ##       ##          ACA



        The program expects a directory path that contains the following formated files:

        pathway : <pathway name>
        output  : <output file name *must be numpy array>

        Note: This is to prepare the data for two types of analysis: clustering and classification

example use:  python genes_sample_swap.py --pathway "dna_repair.json" --output "dna_repair_bysample.json"

'''
