from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sys
sys.path.append('../')
from models.genes_sample_swap import swap_axis
from sklearn.decomposition import PCA

plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

swapped = swap_axis("HALLMARK_HEDGEHOG_SIGNALING.json")
np.savetxt("swapped_hedgehog_signaling.csv", swapped, delimiter=",")




# pca = PCA(n_components=2)
# pca.fit(swapped)

# def draw_vector(v0, v1, ax=None):
#     print(v1)
#     print(v0)
#     ax = ax or plt.gca()
#     arrowprops=dict(arrowstyle='->',
#                     linewidth=2,
#                     shrinkA=0, shrinkB=0)
#     ax.annotate('', v1, v0, arrowprops=arrowprops)
#
# # plot data
# plt.scatter(swapped[:, 0], swapped[:, 1], alpha=0.2)
# for length, vector in zip(pca.explained_variance_, pca.components_):
#     v = vector * 3 * np.sqrt(length)
#     draw_vector(pca.mean_, pca.mean_ + v)
# plt.axis('equal')
