# -*- coding: utf-8 -*-

"""
Anisha Kadri 2017
ak4114@ic.ac.uk

A script that collects data for networks with the following attachment mechanisms:
1) For pure preferential attachement:-
    pref_att(N, m) 
2) For random attachment:-
    rand_att(N,m)
3) For a mixture of the two, attachment via random walk:-
    walk_att(N,m,L)
    
Over a variable number of:
m= initial edges per new node, and
N = Final network size

More detailed variable descriptions are availible in the accommpaying report.

References
----------
[1] A. L. Barabási and R. Albert "Emergence of scaling in
random networks", Science 286, pp 509-512, 1999.

[2] James Clough, Log binning Method: log_bin.py

"""

import numpy as np
import matplotlib.pyplot as plt
import os
import log_bin as lb
import networkx as nx
import model as mod

#Step 1: Setting Variables
m_values = [2,4,8,16,32,64,128] #List of m values to iterate over for fixed N=1e5
N_values = [2,3,4,5,6] #System sizes, specified as powrs of 10, for fixed m=4
total_runs = 1


#Choose a bin exponent, 1 for non logarithmic binning, 1.2 for log binning
bin_exp = 1
#bin_exp = 1.2
    
#Step 2: Creating Networks
#Creating variable m graph, N=1e5, can comment/ uncomment method choosing attachment mechanism
for i in m_values:
    m = i    
    N= 1e5
    run = 1                                     #counter of runs
    data = np.array([])
    while run <= total_runs:
        graph = mod.pref_att(N,m, seed = None)
        #nx.draw(graph)                         #uncomment to draw the graph
        #plt.show()

        graph = mod.rand_att(N,m,seed = None)   #select method of attachment
        #graph = mod.rand_walk(N,m,L,seed=None)
        
         adj_list = nx.to_dict_of_lists(graph)
         degrees = [] 
         for i in range(len(adj_list)):
             degrees.append(len(adj_list[i]))
         degrees = np.array(degrees)
         data = np.append(data,degrees)
         run += 1
        
     k, hist = lb.log_bin(data, bin_start = min(data),first_bin_width=1., a=bin_exp, datatype='float', drop_zeros=True, debug_mode=False) 
     plt.plot(k,hist,'-', label = 'N= %s, m=%s'%(N,m))
    
# plt.xscale('log')
# plt.yscale('log')
# plt.legend()
# plt.xlabel('degree k')
# plt.ylabel('n(k)')
# plt.show()
# plt.clf()


# #Creating variable N graph, m=4, can comment/ uncomment method choosing attachment mechanism
# for i in N_values:
#     m = 4    
#     N= 10**i
#     run = 1
#     data = np.array([])
#     k_max= np.array([])
#     k1_values = np.array([])
#     while run <= total_runs:
#         graph = mod.pref_att(N,m, seed = None)
#         #graph = mod.rand_att(N,m,seed = None)
#         #graph = mod.rand_walk(N,m,L,seed=None)
        
#         adj_list = nx.to_dict_of_lists(graph)
#         degrees = []
#         for i in range(len(adj_list)):
#             degrees.append(len(adj_list[i]))
#         degrees = np.array(degrees)
#         data = np.append(data,degrees)
#         kmax = np.append(k_max, np.max(degrees))
#         run +=1
        
    #To save the average highest expcted degree for system size N:
    # k1_values = np.append(np.average(k_max)) 
    
    # #To generate a histogram of results for N, m=4:
    # k, hist = lb.log_bin(data, bin_start = min(data),first_bin_width=1., a=bin_exp, datatype='float', drop_zeros=True, debug_mode=False) 
    # plt.plot(k,hist,'-', label = 'N= %s, m=%s'%(N,m))

# plt.xscale('log')
# plt.yscale('log')
# plt.legend()
# plt.xlabel('degree k')
# plt.ylabel('n(k)')
# plt.show()
# plt.clf()

# #Finding largest expected degree:
# for i in range(len(N_values)):
#     print "System Size = 10^",N_values[i]
#     print "k_1 observed =",k1_values[i]
    
    



        
