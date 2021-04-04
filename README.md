# Clustering_project_JGaro

Clustering algorithm I did to progress in Python and discover
the principle of Clustering.

I had few struggled making this project but it was interesting to find
solutions for those problem even if sometimes i'm sure that there were not
the best solution.

First problem : computing the distance.
I wasn't able to compute the distance between 2 sequence by implementing
the distance formula in the algorithm. So i used a method from the module
sequence of the skbio library. since a part of the project was to
make my own "Sequence" object i just really used the "Sequence" object of
skbio in the method used to calculate the distance. Another problem
while using this class and method was that it can only be calculate
on sequences of the same length. so i decide to "only" cut the ending
extremity of the longest sequence. in my cases it seems to not raise
some problem with the ending tree, however it may be the case with
other set of sequences if there indel inside of the sequence.

Second problem : class attributes problem.

The second problem I encountered was that the attributes value
of a Cluster object was changed when i passed the value to a variable
and change the value of the created variable in a method of the Cluster 
class (the linkage method). I made a few research and read about 
how to correctly construct a class (something that I realized I was very far to do it the right way...) 
but I didn't find a working solution. The solution I found was to use the
function deepcopy() from the module copy to be able to passed the value
of an attribute to another variable without changing the attribute value
when I'll change the new variable value.

Third problem : Build the newick string format.

In this case I admit that i wasn't really clever at all since
the solution was actually mentioned in the statement of
that part of the project... Well, the problem was that i needed
to transform a list of list of n... list of cluster in a string
that have a specific format with comma and parentheses at the right place.
I tried silly algorithms that were such a mess until someone told me to think 
about making a recursive function. And after a few internet research I was able to do it.






