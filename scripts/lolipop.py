# libraries
import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv('genes.csv')
 
# Reorder it following the values of the first value:
ordered_df = df.sort_values(by='Support Vector Machine Classification Rate')

pathways = ordered_df['Gene Pathway']
new_pathways = []

for pathway in pathways:
	if pathway != "BIG_OL_MATRIX":
		new_pathways.append(pathway[9:])
	else:
		new_pathways.append(pathway)

my_range=range(1,len(df.index)+1)
 
# The vertical plot is made using the hline function
# I load the seaborn library only to benefit the nice looking feature
import seaborn as sns
plt.hlines(y=my_range, xmin=ordered_df['Support Vector Machine Classification Rate'], xmax=ordered_df['K-Nearest Neighbors Classification Rate'], color='grey', alpha=0.4)
plt.scatter(ordered_df['Support Vector Machine Classification Rate'], my_range, color='#518AAD', alpha=1, label='Support Vector Machine Classification Rate')
plt.scatter(ordered_df['K-Nearest Neighbors Classification Rate'], my_range, color='#e59152', alpha=1 , label='K-Nearest Neighbors Classification Rate')
plt.legend()
 
# Add title and axis names
plt.yticks(my_range, new_pathways)
plt.title("Comparison of the value 1 and the value 2", loc='center')
plt.xlabel('Classification Accuracy')
plt.ylabel('Signaling Pathways')

plt.show()