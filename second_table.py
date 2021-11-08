import networkx as nx

London_Rail = nx.read_edgelist('data/London/simple/London_rail_simple.txt', nodetype=int)
London_Drive = nx.read_edgelist('data/London/simple/London_drive_simple.txt', nodetype=int)
London_Walk = nx.read_edgelist('data/London/simple/London_walk_simple.txt', nodetype=int)
London_Bike = nx.read_edgelist('data/London/simple/London_bike_simple.txt', nodetype=int)

Amsterdam_Rail = nx.read_edgelist('data/Amsterdam/simple/Amsterdam_rail_simple.txt', nodetype=int)
Amsterdam_Drive = nx.read_edgelist('data/Amsterdam/simple/Amsterdam_drive_simple.txt', nodetype=int)
Amsterdam_Walk = nx.read_edgelist('data/Amsterdam/simple/Amsterdam_walk_simple.txt', nodetype=int)
Amsterdam_Bike = nx.read_edgelist('data/Amsterdam/simple/Amsterdam_bike_simple.txt', nodetype=int)

Barcelona_Rail = nx.read_edgelist('data/Barcelona/simple/Barcelona_rail_simple.txt', nodetype=int)
Barcelona_Drive = nx.read_edgelist('data/Barcelona/simple/Barcelona_drive_simple.txt', nodetype=int)
Barcelona_Walk = nx.read_edgelist('data/Barcelona/simple/Barcelona_walk_simple.txt', nodetype=int)
Barcelona_Bike = nx.read_edgelist('data/Barcelona/simple/Barcelona_bike_simple.txt', nodetype=int)

LA_Rail = nx.read_edgelist('data/LA/simple/LA_rail_simple.txt', nodetype=int)
LA_Drive = nx.read_edgelist('data/LA/simple/LA_drive_simple.txt', nodetype=int)
LA_Walk = nx.read_edgelist('data/LA/simple/LA_walk_simple.txt', nodetype=int)
LA_Bike = nx.read_edgelist('data/LA/simple/LA_bike_simple.txt', nodetype=int)

Mexico_Rail = nx.read_edgelist('data/Mexico/simple/Mexico_rail_simple.txt', nodetype=int)
Mexico_Drive = nx.read_edgelist('data/Mexico/simple/Mexico_drive_simple.txt', nodetype=int)
Mexico_Walk = nx.read_edgelist('data/Mexico/simple/Mexico_walk_simple.txt', nodetype=int)
Mexico_Bike = nx.read_edgelist('data/Mexico/simple/Mexico_bike_simple.txt', nodetype=int)

Bogota_Rail = nx.read_edgelist('data/Bogota/simple/Bogota_rail_simple.txt', nodetype=int)
Bogota_Drive = nx.read_edgelist('data/Bogota/simple/Bogota_drive_simple.txt', nodetype=int)
Bogota_Walk = nx.read_edgelist('data/Bogota/simple/Bogota_walk_simple.txt', nodetype=int)
Bogota_Bike = nx.read_edgelist('data/Bogota/simple/Bogota_bike_simple.txt', nodetype=int)

Jakarta_Rail = nx.read_edgelist('data/Jakarta/simple/Jakarta_rail_simple.txt', nodetype=int)
Jakarta_Drive = nx.read_edgelist('data/Jakarta/simple/Jakarta_drive_simple.txt', nodetype=int)
Jakarta_Walk = nx.read_edgelist('data/Jakarta/simple/Jakarta_walk_simple.txt', nodetype=int)
Jakarta_Bike = nx.read_edgelist('data/Jakarta/simple/Jakarta_bike_simple.txt', nodetype=int)

Beihai_Rail = nx.read_edgelist('data/Beihai/simple/Beihai_rail_simple.txt', nodetype=int)
Beihai_Drive = nx.read_edgelist('data/Beihai/simple/Beihai_drive_simple.txt', nodetype=int)
Beihai_Walk = nx.read_edgelist('data/Beihai/simple/Beihai_walk_simple.txt', nodetype=int)
Beihai_Bike = nx.read_edgelist('data/Beihai/simple/Beihai_bike_simple.txt', nodetype=int)

Budapest_Rail = nx.read_edgelist('data/Budapest/simple/Budapest_rail_simple.txt', nodetype=int)
Budapest_Drive = nx.read_edgelist('data/Budapest/simple/Budapest_drive_simple.txt', nodetype=int)
Budapest_Walk = nx.read_edgelist('data/Budapest/simple/Budapest_walk_simple.txt', nodetype=int)
Budapest_Bike = nx.read_edgelist('data/Budapest/simple/Budapest_bike_simple.txt', nodetype=int)

Copenhagen_Rail = nx.read_edgelist('data/Copenhagen/simple/Copenhagen_rail_simple.txt', nodetype=int)
Copenhagen_Drive = nx.read_edgelist('data/Copenhagen/simple/Copenhagen_drive_simple.txt', nodetype=int)
Copenhagen_Walk = nx.read_edgelist('data/Copenhagen/simple/Copenhagen_walk_simple.txt', nodetype=int)
Copenhagen_Bike = nx.read_edgelist('data/Copenhagen/simple/Copenhagen_bike_simple.txt', nodetype=int)

Detroit_Rail = nx.read_edgelist('data/Detroit/simple/Detroit_rail_simple.txt', nodetype=int)
Detroit_Drive = nx.read_edgelist('data/Detroit/simple/Detroit_drive_simple.txt', nodetype=int)
Detroit_Walk = nx.read_edgelist('data/Detroit/simple/Detroit_walk_simple.txt', nodetype=int)
Detroit_Bike = nx.read_edgelist('data/Detroit/simple/Detroit_bike_simple.txt', nodetype=int)

Manhattan_Rail = nx.read_edgelist('data/Manhattan/simple/Manhattan_rail_simple.txt', nodetype=int)
Manhattan_Drive = nx.read_edgelist('data/Manhattan/simple/Manhattan_drive_simple.txt', nodetype=int)
Manhattan_Walk = nx.read_edgelist('data/Manhattan/simple/Manhattan_walk_simple.txt', nodetype=int)
Manhattan_Bike = nx.read_edgelist('data/Manhattan/simple/Manhattan_bike_simple.txt', nodetype=int)

Phoenix_Rail = nx.read_edgelist('data/Phoenix/simple/Phoenix_rail_simple.txt', nodetype=int)
Phoenix_Drive = nx.read_edgelist('data/Phoenix/simple/Phoenix_drive_simple.txt', nodetype=int)
Phoenix_Walk = nx.read_edgelist('data/Phoenix/simple/Phoenix_walk_simple.txt', nodetype=int)
Phoenix_Bike = nx.read_edgelist('data/Phoenix/simple/Phoenix_bike_simple.txt', nodetype=int)

Portland_Rail = nx.read_edgelist('data/Portland/simple/Portland_rail_simple.txt', nodetype=int)
Portland_Drive = nx.read_edgelist('data/Portland/simple/Portland_drive_simple.txt', nodetype=int)
Portland_Walk = nx.read_edgelist('data/Portland/simple/Portland_walk_simple.txt', nodetype=int)
Portland_Bike = nx.read_edgelist('data/Portland/simple/Portland_bike_simple.txt', nodetype=int)


def overlap_network(layers):
    """
    Create the overlap network from the different layers.
    The function takes a list of graphs as the different layers of the multilayer network and returns a new graph
    """
    O = nx.Graph()
    for G in layers:
        for i,j,data in G.edges(data=True):
            if O.has_edge(i,j):
                O[i][j]['weight'] += data['weight'] if 'weight' in data else 1.0
            else:
                O.add_edge(i, j, weight= data['weight'] if 'weight' in data else 1.0)
    return O

def avrg_Degree(graph):
    soma = 0
    for x in graph.degree:
        soma = soma + x[1]
    print(f"Average Degree - {soma / len(graph.degree)}")
    return soma / len(graph.degree)

f = open("results/second_table.txt",'w')

############################## LONDON ##############################
G_Layers = [London_Rail, London_Drive, London_Walk, London_Bike]
O = overlap_network(G_Layers)
print("LONDON:")
print("Nodes:" + str(len(O.nodes)))
print("Edges:" + str(len(O.edges)))
f.write("LONDON:\n")
f.write("Nodes:" + str(len(O.nodes)) + "\n")
f.write("Edges:" + str(len(O.edges)) + "\n")
f.write("Average degree:" + str(avrg_Degree(O))+ "\n\n")

############################## AMSTERDAM ##############################
G_Layers = [Amsterdam_Rail, Amsterdam_Drive, Amsterdam_Walk, Amsterdam_Bike]
O = overlap_network(G_Layers)
print("AMSTERDAM:")
print("Nodes:" + str(len(O.nodes)))
print("Edges:" + str(len(O.edges)))
f.write("AMSTERDAM:\n")
f.write("Nodes:" + str(len(O.nodes)) + "\n")
f.write("Edges:" + str(len(O.edges))+ "\n")
f.write("Average degree:" + str(avrg_Degree(O))+ "\n\n")

############################## BARCELONA ##############################
G_Layers = [Barcelona_Rail, Barcelona_Drive, Barcelona_Walk, Barcelona_Bike]
O = overlap_network(G_Layers)
print("BARCELONA:")
print("Nodes:" + str(len(O.nodes)))
print("Edges:" + str(len(O.edges)))
f.write("BARCELONA:\n")
f.write("Nodes:" + str(len(O.nodes)) + "\n")
f.write("Edges:" + str(len(O.edges)) + "\n")
f.write("Average degree:" + str(avrg_Degree(O))+ "\n\n")


############################## LA ##############################
G_Layers = [LA_Rail, LA_Drive, LA_Walk, LA_Bike]
O = overlap_network(G_Layers)
print("LA:")
print("Nodes:" + str(len(O.nodes)))
print("Edges:" + str(len(O.edges)))
f.write("LA:\n")
f.write("Nodes:" + str(len(O.nodes)) + "\n")
f.write("Edges:" + str(len(O.edges)) + "\n")
f.write("Average degree:" + str(avrg_Degree(O))+ "\n\n")

############################## MEXICO ##############################
G_Layers = [Mexico_Rail, Mexico_Drive, Mexico_Walk, Mexico_Bike]
O = overlap_network(G_Layers)
print("Mexico City:")
print("Nodes:" + str(len(O.nodes)))
print("Edges:" + str(len(O.edges)))
f.write("MEXICO CITY:\n")
f.write("Nodes:" + str(len(O.nodes)) + "\n")
f.write("Edges:" + str(len(O.edges)) + "\n")
f.write("Average degree:" + str(avrg_Degree(O))+ "\n\n")

############################## BOGOTA ##############################
G_Layers = [Bogota_Rail, Bogota_Drive, Bogota_Walk, Bogota_Bike]
O = overlap_network(G_Layers)
print("Bogota:")
print("Nodes:" + str(len(O.nodes)))
print("Edges:" + str(len(O.edges)))
f.write("BOGOTA:\n")
f.write("Nodes:" + str(len(O.nodes)) + "\n")
f.write("Edges:" + str(len(O.edges)) + "\n")
f.write("Average degree:" + str(avrg_Degree(O))+ "\n\n")

############################## JAKARTA ##############################
G_Layers = [Jakarta_Rail, Jakarta_Drive, Jakarta_Walk, Jakarta_Bike]
O = overlap_network(G_Layers)
print("Jakarta:")
print("Nodes:" + str(len(O.nodes)))
print("Edges:" + str(len(O.edges)))
f.write("JAKARTA:\n")
f.write("Nodes:" + str(len(O.nodes)) + "\n")
f.write("Edges:" + str(len(O.edges)) + "\n")
f.write("Average degree:" + str(avrg_Degree(O))+ "\n\n")

############################## BEIHAI ##############################
G_Layers = [Beihai_Rail, Beihai_Drive, Beihai_Walk, Beihai_Bike]
O = overlap_network(G_Layers)
print("Beihai:")
print("Nodes:" + str(len(O.nodes)))
print("Edges:" + str(len(O.edges)))
f.write("BEIHAI:\n")
f.write("Nodes:" + str(len(O.nodes)) + "\n")
f.write("Edges:" + str(len(O.edges)) + "\n")
f.write("Average degree:" + str(avrg_Degree(O))+ "\n\n")

############################## BUDAPEST ##############################
G_Layers = [Budapest_Rail, Budapest_Drive, Budapest_Walk, Budapest_Bike]
O = overlap_network(G_Layers)
print("Budapest:")
print("Nodes:" + str(len(O.nodes)))
print("Edges:" + str(len(O.edges)))
f.write("BUDAPEST:\n")
f.write("Nodes:" + str(len(O.nodes)) + "\n")
f.write("Edges:" + str(len(O.edges)) + "\n")
f.write("Average degree:" + str(avrg_Degree(O))+ "\n\n")

############################## COPENHAGEN ##############################
G_Layers = [Copenhagen_Rail, Copenhagen_Drive, Copenhagen_Walk, Copenhagen_Bike]
O = overlap_network(G_Layers)
print("Copenhagen:")
print("Nodes:" + str(len(O.nodes)))
print("Edges:" + str(len(O.edges)))
f.write("COPENHAGEN:\n")
f.write("Nodes:" + str(len(O.nodes)) + "\n")
f.write("Edges:" + str(len(O.edges)) + "\n")
f.write("Average degree:" + str(avrg_Degree(O))+ "\n\n")

############################## DETROIT ##############################
G_Layers = [Detroit_Rail, Detroit_Drive, Detroit_Walk, Detroit_Bike]
O = overlap_network(G_Layers)
print("Detroit:")
print("Nodes:" + str(len(O.nodes)))
print("Edges:" + str(len(O.edges)))
f.write("DETROIT:\n")
f.write("Nodes:" + str(len(O.nodes)) + "\n")
f.write("Edges:" + str(len(O.edges)) + "\n")
f.write("Average degree:" + str(avrg_Degree(O))+ "\n\n")

############################## MANHATTAN ##############################
G_Layers = [Manhattan_Rail, Manhattan_Drive, Manhattan_Walk, Manhattan_Bike]
O = overlap_network(G_Layers)
print("Manhattan:")
print("Nodes:" + str(len(O.nodes)))
print("Edges:" + str(len(O.edges)))
f.write("MANHATTAN:\n")
f.write("Nodes:" + str(len(O.nodes)) + "\n")
f.write("Edges:" + str(len(O.edges)) + "\n")
f.write("Average degree:" + str(avrg_Degree(O))+ "\n\n")

############################## PHOENIX ##############################
G_Layers = [Phoenix_Rail, Phoenix_Drive, Phoenix_Walk, Phoenix_Bike]
O = overlap_network(G_Layers)
print("Phoenix:")
print("Nodes:" + str(len(O.nodes)))
print("Edges:" + str(len(O.edges)))
f.write("PHOENIX:\n")
f.write("Nodes:" + str(len(O.nodes)) + "\n")
f.write("Edges:" + str(len(O.edges)) + "\n")
f.write("Average degree:" + str(avrg_Degree(O))+ "\n\n")

############################## PORTLAND ##############################
G_Layers = [Portland_Rail, Portland_Drive, Portland_Walk, Portland_Bike]
O = overlap_network(G_Layers)
print("Portland:")
print("Nodes:" + str(len(O.nodes)))
print("Edges:" + str(len(O.edges)))
f.write("PORTLAND:\n")
f.write("Nodes:" + str(len(O.nodes)) + "\n")
f.write("Edges:" + str(len(O.edges)) + "\n")
f.write("Average degree:" + str(avrg_Degree(O))+ "\n\n")

f.close()

