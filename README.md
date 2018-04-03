# panTCGA CPSC4300 project

# Notes:

### -This dataset is LARGE, make sure you have like 20GB of free space or use another computer, maybe the palmetto cluster.
### -To save space :), there are two directories in the drive: allfiles and filesforpathwayscript with the data
### -You really only need filesforpathwayscript if you want a submatrix for a specific pathway,
### -After running the script the <pathwayname>.json, the file will appear in the pathways folder

# How to generate new pathway subsets:

## 1)pick a pathway from: gene_dict.json
## 2) call pathwayselector.py

# How to find missing genes:
### Why: There maybe some genes that need to be manually put into hallmark_id_to_ensembles.json
### 1) Get missing gene from error message
### 2) Google: GeneName ensembl id
#### Example: search:"NCR1 ensembl id" 
#### ensembl.org is a good site : For this search: https://useast.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189430;r=19:54906150-54916140
#### Then get the synonym for the gene or update the ensembl id if it doesn't exist
