# Clustering_project_JGaro

Clustering algorithm I did to progress in Python and discover
the principle of Clustering.

I had few struggled making this project but it was interesting to find
solutions for those problem even if sometimes i'm sure there was not
the best.

First problem : computing the distance.
I wasn't able to compute the distance between 2 sequence by implementing
the distance formula in the algoritm. So i used a method from the module
sequence of the skbio library. since the a part of the project was to 
make my own "Sequence" object i just realy use the "Sequence" object of
skbio in the method used to calculate the distance. Another problem
while using this class and method was that it can only be calculate
on sequence of the same length. so i decide to "only" cut the ending
extremity of the longest sequence. in my cases it seems to not raise
some problem with the ending tree, however it may be the case with
other set of sequences.

Second problem : class attributes problem.

The second problem i encontered was that the attributes value
of a Cluster object was change when i passed the value to a variable 
and change this one in a method of the Cluster class (the linkage method).
I made a few research and read about how to correctly construct a class
(something that i realize i was very far to do it the right way...) but
i didn't found a working solution. The solution i found was to use the 
function deepcopy() from the module copy to ba able to passed the value
of an attribute to another variable without changing the attribute value
when I'll change the new variable value.

Third problem : Build the newick string format.

In this case i admit that i wasn't realy clever since
the solution was actualy mentionned in the statement of
that part of the project... well the problem was that i needed
to transform a list of list of n... list of cluster in a string
that have a specific format. I try silly algorithm that were such
a mess until someone told me to think about making a recursive
function. And after a few internet research I was able to do it.









