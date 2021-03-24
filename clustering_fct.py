from skbio.sequence import Sequence as SkSequence
from copy import deepcopy

class Sequence:
    """define a nucleotidic sequence and his associated label

    With this class we have a Sequence assiociated with
    a label that describe it and that can be show in the
    dendrogram. We will be able to get the distance between
    two Sequence with the method distance_to

    """
    def __init__(self,sequence,label=""):
        """init with a sequence as a string, label can be empty"""

        self.sequence = sequence
        self.label = label
    
    def to_string(self):
        """return the nucleotidic sequence as a string"""
        return self.sequence
    
    def to_label(self):
        """return the label as a string"""
        return self.label
    
    
    def distance_to(self, other):
        """return the distance between two sequence

        this method return the distance between two sequence using
        skbio Sequence class and and distance method. While this
        method can only compute distance between sequence with the same
        length we will delete some of the nucleotide of the longest
        sequence.

        """
        if len(self.sequence) > len(other.sequence):
            cut = len(self.sequence)-len(other.sequence)
            self.sequence = self.sequence[0:-cut]
        elif len(other.sequence) > len(self.sequence):
            cut = len(other.sequence) - len(self.sequence)
            other.sequence = other.sequence[0:-cut]
        else:
            pass
        
        skseq_self = SkSequence(self.sequence)
        skseq_other = SkSequence(other.sequence)

        return skseq_self.distance(skseq_other)


class Cluster:
    """A class that define a cluster that can be simple or complex

    cluster with only a sequence are simple , cluster with few
    sequence or sub-cluster are complex. the Class is define
    with the list of the Sequence object, the list of the sequence
    of each Sequence (class) in string, and the label of each
    Sequence.
    
    The method linkage return distance between the cluster and
    another one.

    The method get_newick return the cluster in newick format

    """
    def __init__(self,elements, merging_cluster = None):
        """Constructor depending of the elements past in parameters

        the constructor will init the cluster differently depending of
        the parameters:
        if there is just a sequence, it will create a simple cluster.
        if there is a list of Sequence it will create a complex cluster
        with all the Sequence in the "root".
        if there is two cluster it will create a new cluster adding
        the second one to the root of the first.

        """
        if type(elements) == Sequence:
            self.cluster_elements = elements
            self.cluster_elements_str = elements.to_string()
            self.cluster_elements_labels = elements.to_label()

        elif type(elements) == list:
            
            self.cluster_elements = elements

            self.cluster_elements_labels = []
            for i in range(0, len(elements)):
                self.cluster_elements_labels.append(elements[i].to_label())
            
            self.cluster_elements_str = []
            for i in range(0, len(elements)):
                self.cluster_elements_str.append(elements[i].to_string())

        elif type(elements) == Cluster and merging_cluster != None:
            
            self.cluster_elements = []
            self.cluster_elements.append(elements.cluster_elements)
            self.cluster_elements.append(merging_cluster.cluster_elements)
            
            self.cluster_elements_str = []
            self.cluster_elements_str.append(elements.cluster_elements_str)
            self.cluster_elements_str.append(
                                      merging_cluster.cluster_elements_str)

            self.cluster_elements_labels = []
            self.cluster_elements_labels.append(elements.cluster_elements_labels)
            self.cluster_elements_labels.append(
                                      merging_cluster.cluster_elements_labels)


        else:
            raise Exception("Error : \"elements\" argument must be list "
                            "or str or Cluster class "
                            "not {}".format(type(elements)))


    def get_cluster_elements(self):
        """return the list of the Sequence object of the cluster"""
        
        copy = deepcopy(self.cluster_elements)
        return copy

    def get_cluster_elements_str(self):
        """return the list of the sequence of the cluster as strings"""

        copy = deepcopy(self.cluster_elements_str)
        return copy
    
    def get_cluster_elements_labels(self):
        """return the list of the labels of the cluster as strings"""
        
        copy = deepcopy(self.cluster_elements_labels)
        return copy


    def linkage(self, other):
        """return the distance between the cluster and another one

        the distance between two cluster will be the average
        distance between all the distance from all the combinations
        of sequence between the two cluster.
        """
        
        distance = 0
        list1 = self.get_cluster_elements()
        list2 = other.get_cluster_elements()
        lenght = 0
        t = 0
        
        #first it "de-clusterize" the cluster into a simple list
        #of Sequence.
        done = False
        while done == False:
            done = True
            try:
                for i in range(0,len(list1)):
                    if type(list1[i]) != Sequence:
                        for j in range(0,len(list1[i])):
                            list1.append(list1[i][j])
                        list1.pop(i)
                        done = False
            except:

                pass
            
        try:
            lenght = len(list1)
        except:
            lenght += 1
            empty_list = []
            empty_list.append(list1)
            list1 = empty_list

        
        #it do the same for the second cluster
        done = False
        while done == False:
            done = True
            try:
                for i in range(0,len(list2)):
                    if type(list2[i]) != Sequence:
                        for j in range(0,len(list2[i])):
                            list2.append(list2[i][j])
                        list2.pop(i)
                        done = False
            except:
                pass

        try:
            lenght += len(list2)
        except:
            lenght += 1
            empty_list = []
            empty_list.append(list2)
            list2 = empty_list

        #then it calculate the total of all the distance...
        for i in range(0,len(list1)):
            for j in range(0,len(list2)):
                t += list1[i].distance_to(list2[j])

        #...and get the average distance (lenght is the sum of the lenght of)
        #the two cluster.
        distance = t/lenght 
        return distance


    def get_newick(self):
        """return the cluster as newick format
        
        use the get_newick_intermediate() recursive function to go 
        through the different layer of the list of the cluster and
        rebuilt the tree
        
        """
        tree_list = self.get_cluster_elements_labels()
        newick = "("
        
        
        newick = get_newick_intermediate(tree_list,newick,False)

        newick = newick[0] + ");"

        return newick



def get_newick_intermediate(tree_list,newick, end):
    """recursive functions that finaly return a newick format of the cluster
    
    the function goes as "deeper" in the layer of list of each elements in
    the root of the main cluster and put "," , "(" , or ")" when necessary.
    And also put the Label when it encounter a string type of variable.
    end variable become True if the algorithm is about to start to
    treat a new list and that the last element was a list too.

    """
    for i in range(0,len(tree_list)):

        if type(tree_list[i]) == list:
            if end == True:
                newick = newick + ","
                end = False
            newick = newick + "("
            newick, end = get_newick_intermediate(tree_list[i],newick,end)
            newick = newick + ")"

        elif type(tree_list[i]) == str:

            newick = newick + tree_list[i]
            if i != len(tree_list)-1:
                newick = newick + ","

            else:
                end = True

    return newick, end



def clustering(cluster_list):
    """clusterize a list of cluster, base on the distance between them

    the algorithm will computing all the distance within all the
    cluster of the lists (expect between the same), then it will 
    merge the two that shows seems the closest, creating a new cluster,
    and remove the two that was merged in one. The loop will continue 
    untill there is only one cluster left in the list, then it return 
    this cluster.

    """
    while len(cluster_list) > 1:
        x = 0
        y = 0
        distance_min = 10

        for i in range(0,len(cluster_list)):

            for j in range(0,len(cluster_list)):

                if i != j:
                    distance = cluster_list[i].linkage(cluster_list[j])
                    if distance < distance_min:
                        x = i
                        y = j
                        distance_min = distance
        
        
        clusX = cluster_list[x]
        clusY = cluster_list[y]
        cluster_list.pop(cluster_list.index(clusX))
        cluster_list.pop(cluster_list.index(clusY))

        cluster_list.append(Cluster(clusX,clusY))
    return cluster_list[0]
