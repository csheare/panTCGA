# panTCGA CPSC4300 project

# Notes:
## This dataset is LARGE, make sure you have like 20GB of free space or use another computer, maybe the palmetto cluster.
### To save space :), there are two directories in the drive: allfiles and filesforpathwayscript
### You really only need filesforpathwayscriptif you want a submatrix for a specific pathway,
### After running the script the <pathwayname>.json file will appear in the pathways folder

# How to generate new pathway subsets:
## 1)pick a pathway from: gene_dict.json
## 2) call pathwayselector.py
### Note: there maybe some genes that need to be manually put into hallmark_id_to_ensembles.json, just give the missing gene a google, example search: <GeneName> ensemble id, then replace the missing gene with the gene name synonym, this maybe "unfun" but fixing 5 genes out of like 150 is not that bad :)
