"""
Anisha Kadri 2017
ak4114@ic.ac.uk

A Module containing methods to create networks from different models.

1) For pure preferential attachement:-
    pref_att(N, m) 

2) For random attachment:-
    rand_att(N,m)

3) For a mixture of the two, attachment via random walk:-
    walk_att(N,m,L)

References
----------
[1] A. L. Barabási and R. Albert "Emergence of scaling in
random networks", Science 286, pp 509-512, 1999.
"""
import networkx as nx
import random
import math

def pref_att(N, m, seed=None):
    """Returns a graph that is created using the Barabasi-Albert Model, 
    of N nodes in total and a node with m edges added at each time increment.
    
    Parameters
    ----------
    n = total number of nodes
    m = number of edges attached to each new node, or degree of new node.
    (value must be < N)
    seed = optional argument, initialises random number generator to a starting state.

    Returns
    -------
    A Barabasi Albert Graph, with pure preferential attachment.

    """
    #this ensures that the maximum degree is always less than number of nodes
    if m >= N:
        raise Exception("m-value must be less than N")
    if m < 1:
        raise Exception("graph gowth is sub-critical.Degree of new node cannot be 0")
    
    # Intialises the pseudo-random number generator, allowing result replication.
    random.seed(seed) 
        
    # Creates new graph of m nodes, of equal degree
    nodes = list(range(m))
    G = nx.complete_graph(m)
    G.name = "Graph with N = %s, m = %s"%(N,m)
    
    # Target nodes for new edges
    attach_list = nodes
    
    # Maintains a list of nodes for random sampling,
    # a concantenated edge list
    # thus, number of instances of each node in the list is proportional to it's degree 
    # (i.e. the list has k_i instances of node i)
    node_list=[]
    for i in nodes:
        node_list.extend([i]*m) 
    
    N_tot = m # N_tot = No. of nodes in network, also index numbering for new node
    while N_tot < N:
        new_stubs = [N_tot]*m #create new stubs
        new_edges = zip(new_stubs,attach_list) #create new edges between chosen nodes
        G.add_edges_from(new_edges)
        
        #add new edges to the list
        node_list.extend(attach_list)
        node_list.extend(new_stubs)
        
        # m nodes are chosen from the edge_list to form new targets.
        attach_list = set() # making this a set ensures that edges added are all unique (not a multigraph)
        while len(attach_list)< m:
            random_node =random.choice(node_list)
            attach_list.add(random_node)
        N_tot += 1
        attach_list = list(attach_list)
    return G

def rand_att(N,m, seed=None):
    if m >= N:
        raise Exception("m-value must be less than N")
    if m < 1:
        raise Exception("graph gowth is sub-critical.Degree of new node cannot be 0")
    
    # Intialises the pseudo-random number generator, allowing result replication.
    random.seed(seed) 
        
    # Creates new graph of m nodes, and no edges
    G = nx.generators.classic.empty_graph(m)
    G.name = "Graph with N = %s, m = %s"%(N,m)
    
    # Target nodes for new edges
    attach_list = nx.nodes(G)
    
    N_tot = m # N_tot = No. of nodes in network, also index numbering for new node
    while N_tot < N:
        new_stubs = [N_tot]*m #create new stubs
        new_edges = zip(new_stubs,attach_list) #create new edges between chosen nodes
        G.add_edges_from(new_edges)
        node_list = nx.nodes(G)
        
        # m nodes are chosen at random from the node_list to form new targets.
        attach_list =random.sample(node_list, m)
        N_tot += 1
    return G
    
def random_walk(N,m, L, seed = None):
    if m >= N:
        raise Exception("m-value must be less than N")
    if m < 1:
        raise Exception("graph gowth is sub-critical.Degree of new node cannot be 0")
    
    # Intialises the pseudo-random number generator, allowing result replication.
    random.seed(seed) 
        
    # Creates new graph of m nodes, of equal degree
    G = nx.complete_graph(m)
    nodes = list(range(m))
    # Target nodes for new edges
    attach_list = nodes
    
    N_tot = m # N_tot = No. of nodes in network, also index numbering for new node
    while N_tot < N:
        new_stubs = [N_tot]*m #create new stubs
        new_edges = zip(new_stubs,attach_list) #create new edges between chosen nodes
        G.add_edges_from(new_edges)

        node_list = nx.nodes(G)
        # m nodes are chosen from the edge_list to form new targets.
        attach_list = set() # making this a set ensures that edges added are all unique (not a multigraph)
        random_list = set()
        
        #uniformly choose start point of walk
        while len(random_list)< m:
            random_node =random.choice(node_list)
            random_list.add(random_node)
        N_tot += 1
        
        #take a random walk of length L
        for i in random_list:
            node = i
            steps=0
            if steps<= L:
                neighbours = G.neighbours(node)
                random_node =random.choice(neighbours)
                node = random_node
                steps += 1 
            attach_list.add(node)
        attach_list = list(attach_list)
    return G