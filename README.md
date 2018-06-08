# barabasialbert
# Code to investigate Degree Distributions in Barabasi Albert Networks
# For comparison, three network models are used;
#  1) random attachment mechanism (each node is connected with equal probability P= 1/N)
#  2) pure preferential attachment (each node is connected with probability proportional to number of edges)
#  3) random walk mechanism (a starting point is chosen at random and a walk is intitated of length L to select the end point #of the edge)
#
# A full discussion of the models is availible in the pdf report.
#
# Scripts:
# ‘Run.py' is the main source code from which network data was generated.
# 
# There are two modules in the folder which are required for the script to run.

# The ‘models.py’ contains the methods for network growth via the different attachment mechanisms.

# The ‘log_bin.py’ contains the method for logarithmic binning (written by James Clough).
