from itertools import product
import networkx as nx


def overlap_network(layers):
    """
    Create the overlap network from the different layers.
    The function takes a list of graphs as the different layers of the multilayer network and returns a new graph
    """
    O = nx.Graph()
    for G in layers:
        for i, j, data in G.edges(data=True):
            if O.has_edge(i, j):
                O[i][j]['weight'] += data['weight'] if 'weight' in data else 1.0
            else:
                O.add_edge(i, j, weight=data['weight'] if 'weight' in data else 1.0)
    return O


def overlap_degree_vectors(O, layers, weight=True):
    """
    Get the degree of the nodes in the different layers.

    Returns a dict where the keys are the nodes and the values are lists containing the degree in each layer.

    O Overlapping network
    layers list of layers as networkx graphs
    Weight True for calculate the weighted degree.

    Parameters
    ----------
    O : networkx graph
        Overlap network
    layers : list
        networkx graphs
    weight : Boolean
        True, calculate the weighted degree
    Returns
    -------
    degree_nodes_dict : dict
    """
    degree_nodes_dict = {}
    if weight == True:
        for n in O.nodes():
            deg_temp = []
            deg_temp.append(O.degree(n, weight='weight'))
            for G in layers:
                if n in G.nodes():
                    deg_temp.append(G.degree(n, weight='weight'))
                else:
                    deg_temp.append(0)
            degree_nodes_dict[n] = deg_temp
    else:
        for n in O.nodes():
            deg_temp = []
            deg_temp.append(O.degree(n))
            for G in layers:
                if n in G.nodes():
                    deg_temp.append(G.degree(n))
                else:
                    deg_temp.append(0)
            degree_nodes_dict[n] = deg_temp

    return degree_nodes_dict


def overlap_census(nodes_degree_dict):
    all_node_degree_vector = list(nodes_degree_dict.values())
    census = {}
    for p in product((0, 1), repeat=len(all_node_degree_vector[0][1:])):
        val = 0
        for node in all_node_degree_vector:
            if list(p) == [1 if i else 0 for i in node[1:]]:
                val += 1
        census[str(p)] = val
    return census


# Transform the data into graphs and then make all the multi-layered graphs by city(by alphabetical order), calculate their overlap census(oc) and add all cities' oc to a vector to plot them in the end
census_vec = []

Amsterdam_bike = nx.read_edgelist("data/Amsterdam/simple/Amsterdam_bike_simple.txt", nodetype=int)
Amsterdam_drive = nx.read_edgelist("data/Amsterdam/simple/Amsterdam_drive_simple.txt", nodetype=int)
Amsterdam_pedestrian = nx.read_edgelist("data/Amsterdam/simple/Amsterdam_walk_simple.txt", nodetype=int)
Amsterdam_rail = nx.read_edgelist("data/Amsterdam/simple/Amsterdam_rail_simple.txt", nodetype=int)

Amsterdam_Layers = [Amsterdam_bike, Amsterdam_drive, Amsterdam_pedestrian, Amsterdam_rail]
Amsterdam_overlap = overlap_network(Amsterdam_Layers)
Amsterdam_nodes_degree_dict = overlap_degree_vectors(Amsterdam_overlap, Amsterdam_Layers, weight=False)
Amsterdam_overlap_census = overlap_census(Amsterdam_nodes_degree_dict)
census_vec.append([Amsterdam_overlap_census, Amsterdam_overlap])

Barcelona_bike = nx.read_edgelist("data/Barcelona/simple/Barcelona_bike_simple.txt", nodetype=int)
Barcelona_drive = nx.read_edgelist("data/Barcelona/simple/Barcelona_drive_simple.txt", nodetype=int)
Barcelona_pedestrian = nx.read_edgelist("data/Barcelona/simple/Barcelona_walk_simple.txt", nodetype=int)
Barcelona_rail = nx.read_edgelist("data/Barcelona/simple/Barcelona_rail_simple.txt", nodetype=int)

Barcelona_Layers = [Barcelona_bike, Barcelona_drive, Barcelona_pedestrian, Barcelona_rail]
Barcelona_overlap = overlap_network(Barcelona_Layers)
Barcelona_nodes_degree_dict = overlap_degree_vectors(Barcelona_overlap, Barcelona_Layers, weight=False)
Barcelona_overlap_census = overlap_census(Barcelona_nodes_degree_dict)
census_vec.append([Barcelona_overlap_census, Barcelona_overlap])

Beihai_bike = nx.read_edgelist("data/Beihai/simple/Beihai_bike_simple.txt", nodetype=int)
Beihai_drive = nx.read_edgelist("data/Beihai/simple/Beihai_drive_simple.txt", nodetype=int)
Beihai_pedestrian = nx.read_edgelist("data/Beihai/simple/Beihai_walk_simple.txt", nodetype=int)
Beihai_rail = nx.read_edgelist("data/Beihai/simple/Beihai_rail_simple.txt", nodetype=int)

Beihai_Layers = [Beihai_bike, Beihai_drive, Beihai_pedestrian, Beihai_rail]
Beihai_overlap = overlap_network(Beihai_Layers)
Beihai_nodes_degree_dict = overlap_degree_vectors(Beihai_overlap, Beihai_Layers, weight=False)
Beihai_overlap_census = overlap_census(Beihai_nodes_degree_dict)
census_vec.append([Beihai_overlap_census, Beihai_overlap])

Bogota_bike = nx.read_edgelist("data/Bogota/simple/Bogota_bike_simple.txt", nodetype=int)
Bogota_drive = nx.read_edgelist("data/Bogota/simple/Bogota_drive_simple.txt", nodetype=int)
Bogota_pedestrian = nx.read_edgelist("data/Bogota/simple/Bogota_walk_simple.txt", nodetype=int)
Bogota_rail = nx.read_edgelist("data/Bogota/simple/Bogota_rail_simple.txt", nodetype=int)

Bogota_Layers = [Bogota_bike, Bogota_drive, Bogota_pedestrian, Bogota_rail]
Bogota_overlap = overlap_network(Bogota_Layers)
Bogota_nodes_degree_dict = overlap_degree_vectors(Bogota_overlap, Bogota_Layers, weight=False)
Bogota_overlap_census = overlap_census(Bogota_nodes_degree_dict)
census_vec.append([Bogota_overlap_census, Bogota_overlap])

Budapest_bike = nx.read_edgelist("data/Budapest/simple/Budapest_bike_simple.txt", nodetype=int)
Budapest_drive = nx.read_edgelist("data/Budapest/simple/Budapest_drive_simple.txt", nodetype=int)
Budapest_pedestrian = nx.read_edgelist("data/Budapest/simple/Budapest_walk_simple.txt", nodetype=int)
Budapest_rail = nx.read_edgelist("data/Budapest/simple/Budapest_rail_simple.txt", nodetype=int)

Budapest_Layers = [Budapest_bike, Budapest_drive, Budapest_pedestrian, Budapest_rail]
Budapest_overlap = overlap_network(Budapest_Layers)
Budapest_nodes_degree_dict = overlap_degree_vectors(Budapest_overlap, Budapest_Layers, weight=False)
Budapest_overlap_census = overlap_census(Budapest_nodes_degree_dict)
census_vec.append([Budapest_overlap_census, Budapest_overlap])

Copenhagen_bike = nx.read_edgelist("data/Copenhagen/simple/Copenhagen_bike_simple.txt", nodetype=int)
Copenhagen_drive = nx.read_edgelist("data/Copenhagen/simple/Copenhagen_drive_simple.txt", nodetype=int)
Copenhagen_pedestrian = nx.read_edgelist("data/Copenhagen/simple/Copenhagen_walk_simple.txt", nodetype=int)
Copenhagen_rail = nx.read_edgelist("data/Copenhagen/simple/Copenhagen_rail_simple.txt", nodetype=int)

Copenhagen_Layers = [Copenhagen_bike, Copenhagen_drive, Copenhagen_pedestrian, Copenhagen_rail]
Copenhagen_overlap = overlap_network(Copenhagen_Layers)
Copenhagen_nodes_degree_dict = overlap_degree_vectors(Copenhagen_overlap, Copenhagen_Layers, weight=False)
Copenhagen_overlap_census = overlap_census(Copenhagen_nodes_degree_dict)
census_vec.append([Copenhagen_overlap_census, Copenhagen_overlap])

Detroit_bike = nx.read_edgelist("data/Detroit/simple/Detroit_bike_simple.txt", nodetype=int)
Detroit_drive = nx.read_edgelist("data/Detroit/simple/Detroit_drive_simple.txt", nodetype=int)
Detroit_pedestrian = nx.read_edgelist("data/Detroit/simple/Detroit_walk_simple.txt", nodetype=int)
Detroit_rail = nx.read_edgelist("data/Detroit/simple/Detroit_rail_simple.txt", nodetype=int)

Detroit_Layers = [Detroit_bike, Detroit_drive, Detroit_pedestrian, Detroit_rail]
Detroit_overlap = overlap_network(Detroit_Layers)
Detroit_nodes_degree_dict = overlap_degree_vectors(Detroit_overlap, Detroit_Layers, weight=False)
Detroit_overlap_census = overlap_census(Detroit_nodes_degree_dict)
census_vec.append([Detroit_overlap_census, Detroit_overlap])

Jakarta_bike = nx.read_edgelist("data/Jakarta/simple/Jakarta_bike_simple.txt", nodetype=int)
Jakarta_drive = nx.read_edgelist("data/Jakarta/simple/Jakarta_drive_simple.txt", nodetype=int)
Jakarta_pedestrian = nx.read_edgelist("data/Jakarta/simple/Jakarta_walk_simple.txt", nodetype=int)
Jakarta_rail = nx.read_edgelist("data/Jakarta/simple/Jakarta_rail_simple.txt", nodetype=int)

Jakarta_Layers = [Jakarta_bike, Jakarta_drive, Jakarta_pedestrian, Jakarta_rail]
Jakarta_overlap = overlap_network(Jakarta_Layers)
Jakarta_nodes_degree_dict = overlap_degree_vectors(Jakarta_overlap, Jakarta_Layers, weight=False)
Jakarta_overlap_census = overlap_census(Jakarta_nodes_degree_dict)
census_vec.append([Jakarta_overlap_census, Jakarta_overlap])

LA_bike = nx.read_edgelist("data/LA/simple/LA_bike_simple.txt", nodetype=int)
LA_drive = nx.read_edgelist("data/LA/simple/LA_drive_simple.txt", nodetype=int)
LA_pedestrian = nx.read_edgelist("data/LA/simple/LA_walk_simple.txt", nodetype=int)
LA_rail = nx.read_edgelist("data/LA/simple/LA_rail_simple.txt", nodetype=int)

LA_Layers = [LA_bike, LA_drive, LA_pedestrian, LA_rail]
LA_overlap = overlap_network(LA_Layers)
LA_nodes_degree_dict = overlap_degree_vectors(LA_overlap, LA_Layers, weight=False)
LA_overlap_census = overlap_census(LA_nodes_degree_dict)
census_vec.append([LA_overlap_census, LA_overlap])

London_bike = nx.read_edgelist("data/London/simple/London_bike_simple.txt", nodetype=int)
London_drive = nx.read_edgelist("data/London/simple/London_drive_simple.txt", nodetype=int)
London_pedestrian = nx.read_edgelist("data/London/simple/London_walk_simple.txt", nodetype=int)
London_rail = nx.read_edgelist("data/London/simple/London_rail_simple.txt", nodetype=int)

London_Layers = [London_bike, London_drive, London_pedestrian, London_rail]
London_overlap = overlap_network(London_Layers)
London_nodes_degree_dict = overlap_degree_vectors(London_overlap, London_Layers, weight=False)
London_overlap_census = overlap_census(London_nodes_degree_dict)
census_vec.append([London_overlap_census, London_overlap])

Manhattan_bike = nx.read_edgelist("data/Manhattan/simple/Manhattan_bike_simple.txt", nodetype=int)
Manhattan_drive = nx.read_edgelist("data/Manhattan/simple/Manhattan_drive_simple.txt", nodetype=int)
Manhattan_pedestrian = nx.read_edgelist("data/Manhattan/simple/Manhattan_walk_simple.txt", nodetype=int)
Manhattan_rail = nx.read_edgelist("data/Manhattan/simple/Manhattan_rail_simple.txt", nodetype=int)

Manhattan_Layers = [Manhattan_bike, Manhattan_drive, Manhattan_pedestrian, Manhattan_rail]
Manhattan_overlap = overlap_network(Manhattan_Layers)
Manhattan_nodes_degree_dict = overlap_degree_vectors(Manhattan_overlap, Manhattan_Layers, weight=False)
Manhattan_overlap_census = overlap_census(Manhattan_nodes_degree_dict)
census_vec.append([Manhattan_overlap_census, Manhattan_overlap])

Mexico_bike = nx.read_edgelist("data/Mexico/simple/Mexico_bike_simple.txt", nodetype=int)
Mexico_drive = nx.read_edgelist("data/Mexico/simple/Mexico_drive_simple.txt", nodetype=int)
Mexico_pedestrian = nx.read_edgelist("data/Mexico/simple/Mexico_walk_simple.txt", nodetype=int)
Mexico_rail = nx.read_edgelist("data/Mexico/simple/Mexico_rail_simple.txt", nodetype=int)

Mexico_Layers = [Mexico_bike, Mexico_drive, Mexico_pedestrian, Mexico_rail]
Mexico_overlap = overlap_network(Mexico_Layers)
Mexico_nodes_degree_dict = overlap_degree_vectors(Mexico_overlap, Mexico_Layers, weight=False)
Mexico_overlap_census = overlap_census(Mexico_nodes_degree_dict)
census_vec.append([Mexico_overlap_census, Mexico_overlap])

Phoenix_bike = nx.read_edgelist("data/Phoenix/simple/Phoenix_bike_simple.txt", nodetype=int)
Phoenix_drive = nx.read_edgelist("data/Phoenix/simple/Phoenix_drive_simple.txt", nodetype=int)
Phoenix_pedestrian = nx.read_edgelist("data/Phoenix/simple/Phoenix_walk_simple.txt", nodetype=int)
Phoenix_rail = nx.read_edgelist("data/Phoenix/simple/Phoenix_rail_simple.txt", nodetype=int)

Phoenix_Layers = [Phoenix_bike, Phoenix_drive, Phoenix_pedestrian, Phoenix_rail]
Phoenix_overlap = overlap_network(Phoenix_Layers)
Phoenix_nodes_degree_dict = overlap_degree_vectors(Phoenix_overlap, Phoenix_Layers, weight=False)
Phoenix_overlap_census = overlap_census(Phoenix_nodes_degree_dict)
census_vec.append([Phoenix_overlap_census, Phoenix_overlap])

Portland_bike = nx.read_edgelist("data/Portland/simple/Portland_bike_simple.txt", nodetype=int)
Portland_drive = nx.read_edgelist("data/Portland/simple/Portland_drive_simple.txt", nodetype=int)
Portland_pedestrian = nx.read_edgelist("data/Portland/simple/Portland_walk_simple.txt", nodetype=int)
Portland_rail = nx.read_edgelist("data/Portland/simple/Portland_rail_simple.txt", nodetype=int)

Portland_Layers = [Portland_bike, Portland_drive, Portland_pedestrian, Portland_rail]
Portland_overlap = overlap_network(Portland_Layers)
Portland_nodes_degree_dict = overlap_degree_vectors(Portland_overlap, Portland_Layers, weight=False)
Portland_overlap_census = overlap_census(Portland_nodes_degree_dict)
census_vec.append([Portland_overlap_census, Portland_overlap])

# Get the overlap census for the pedestrian-drive network to each city
for census in census_vec:
    print(census[0].get('(0, 1, 1, 0)') / len(census[1].nodes))
