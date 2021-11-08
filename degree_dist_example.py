import matplotlib.pyplot as plt
import networkx as nx

# Transform Amsterdam's bike network data to a graph, obtain its degree distribution and then plot it
Amsterdam_bike = nx.read_edgelist("data/Amsterdam/simple/Amsterdam_bike_simple.txt", nodetype=int)
degrees = [Amsterdam_bike.degree(n) for n in Amsterdam_bike.nodes()]
plt.hist(degrees)
plt.xlabel('Degree (k)')
plt.ylabel('Node count')
plt.show()

