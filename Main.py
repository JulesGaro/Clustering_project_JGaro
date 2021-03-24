"""Clustering algorithm that built a dendrogram from
fasta sequence computing distance between nucleotidic sequences test2
"""

__authors__ = "Jules Garreau"
__contact__ = "jules.garreau00@gmail.com"
__version__ = "1.0.0"
__copyright__ = "copyleft"
__date__  = "23/03/21"

import clustering_fct as fct

import dendropy as dp
import os

#get the folder where the programm will load the fasta sequence
path = __file__.split("Main.py")
path = path[0]
path = path + "hemoglobin"
os.chdir(path)

#create list of Sequence object for each fasta sequence
#(for info on the class Sequence see clustering_fct.py)
files = os.listdir()
sequence_list = []

for i in range(0,len(files)):
    with open(files[i], "r") as fasta_file:
        fasta_seq = fasta_file.read()
    
    fasta_seq = fasta_seq.splitlines()
    fasta_seq.pop(0)
    first_fasta_seq = []
    for j in range(0,len(fasta_seq)):
        try:
            if fasta_seq[j][0] == "\n":
                break
            
            first_fasta_seq.append(fasta_seq[j])
        except:
            break
    first_fasta_seq = "".join(first_fasta_seq)
    first_fasta_seq.strip()
    sequence_list.append(fct.Sequence(first_fasta_seq, files[i]))


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
