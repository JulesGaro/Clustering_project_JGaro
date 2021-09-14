"""Clustering algorithm that built a dendrogram from
fasta sequence computing distance between nucleotidic sequences
"""

__authors__ = "Jules Garreau"
__contact__ = "jules.garreau00@gmail.com"
__version__ = "1.0.1"
__copyright__ = "copyleft"
__date__  = "23/03/21"

import clustering_fct as fct

import dendropy as dp
import os

#get the folder where the programm will load the fasta sequence
fct.choose_directory()

#create list of Sequence object for each sequence in each fasta sequence
#(for info on the class Sequence see clustering_fct.py)
files = os.listdir()
sequence_list = fct.get_sequence_list(files)

#create a list of simple cluster (containing only one sequence)
#for all the sequence in sequence_list
cluster_list = []
for i in range(0,len(sequence_list)):
    cluster_list.append(fct.Cluster(sequence_list[i]))

#clusterize the list by computing the distance between cluster
#(for more info on the function clustering() see clustering_fct.py)
clustered_cluster = fct.clustering(cluster_list)

#get the tree of the "root" cluster in newick format
newick = clustered_cluster.get_newick()

#construct and plot the dendrogram 
tree = dp.Tree.get(data = newick, schema = "newick")
tree.print_plot()

#test de changements