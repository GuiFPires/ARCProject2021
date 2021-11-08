import networkx as nx

# Transform the data into graphs(by cities' alphabetical order), add them to a list and in the end print each graph's nodes, links and average degree to then add them to a table
graph_list = []

Amsterdam_bike = nx.read_edgelist("data/Amsterdam/simple/Amsterdam_bike_simple.txt", nodetype=int)
graph_list.append(Amsterdam_bike)
Amsterdam_drive = nx.read_edgelist("data/Amsterdam/simple/Amsterdam_drive_simple.txt", nodetype=int)
graph_list.append(Amsterdam_drive)
Amsterdam_pedestrian = nx.read_edgelist("data/Amsterdam/simple/Amsterdam_walk_simple.txt", nodetype=int)
graph_list.append(Amsterdam_pedestrian)
Amsterdam_rail = nx.read_edgelist("data/Amsterdam/simple/Amsterdam_rail_simple.txt", nodetype=int)
graph_list.append(Amsterdam_rail)

Barcelona_bike = nx.read_edgelist("data/Barcelona/simple/Barcelona_bike_simple.txt", nodetype=int)
graph_list.append(Barcelona_bike)
Barcelona_drive = nx.read_edgelist("data/Barcelona/simple/Barcelona_drive_simple.txt", nodetype=int)
graph_list.append(Barcelona_drive)
Barcelona_pedestrian = nx.read_edgelist("data/Barcelona/simple/Barcelona_walk_simple.txt", nodetype=int)
graph_list.append(Barcelona_pedestrian)
Barcelona_rail = nx.read_edgelist("data/Barcelona/simple/Barcelona_rail_simple.txt", nodetype=int)
graph_list.append(Barcelona_rail)

Beihai_bike = nx.read_edgelist("data/Beihai/simple/Beihai_bike_simple.txt", nodetype=int)
graph_list.append(Beihai_bike)
Beihai_drive = nx.read_edgelist("data/Beihai/simple/Beihai_drive_simple.txt", nodetype=int)
graph_list.append(Beihai_drive)
Beihai_pedestrian = nx.read_edgelist("data/Beihai/simple/Beihai_walk_simple.txt", nodetype=int)
graph_list.append(Beihai_pedestrian)
Beihai_rail = nx.read_edgelist("data/Beihai/simple/Beihai_rail_simple.txt", nodetype=int)
graph_list.append(Beihai_rail)

Bogota_bike = nx.read_edgelist("data/Bogota/simple/Bogota_bike_simple.txt", nodetype=int)
graph_list.append(Bogota_bike)
Bogota_drive = nx.read_edgelist("data/Bogota/simple/Bogota_drive_simple.txt", nodetype=int)
graph_list.append(Bogota_drive)
Bogota_pedestrian = nx.read_edgelist("data/Bogota/simple/Bogota_walk_simple.txt", nodetype=int)
graph_list.append(Bogota_pedestrian)
Bogota_rail = nx.read_edgelist("data/Bogota/simple/Bogota_rail_simple.txt", nodetype=int)
graph_list.append(Bogota_rail)

Budapest_bike = nx.read_edgelist("data/Budapest/simple/Budapest_bike_simple.txt", nodetype=int)
graph_list.append(Budapest_bike)
Budapest_drive = nx.read_edgelist("data/Budapest/simple/Budapest_drive_simple.txt", nodetype=int)
graph_list.append(Budapest_drive)
Budapest_pedestrian = nx.read_edgelist("data/Budapest/simple/Budapest_walk_simple.txt", nodetype=int)
graph_list.append(Budapest_pedestrian)
Budapest_rail = nx.read_edgelist("data/Budapest/simple/Budapest_rail_simple.txt", nodetype=int)
graph_list.append(Budapest_rail)

Copenhagen_bike = nx.read_edgelist("data/Copenhagen/simple/Copenhagen_bike_simple.txt", nodetype=int)
graph_list.append(Copenhagen_bike)
Copenhagen_drive = nx.read_edgelist("data/Copenhagen/simple/Copenhagen_drive_simple.txt", nodetype=int)
graph_list.append(Copenhagen_drive)
Copenhagen_pedestrian = nx.read_edgelist("data/Copenhagen/simple/Copenhagen_walk_simple.txt", nodetype=int)
graph_list.append(Copenhagen_pedestrian)
Copenhagen_rail = nx.read_edgelist("data/Copenhagen/simple/Copenhagen_rail_simple.txt", nodetype=int)
graph_list.append(Copenhagen_rail)

Detroit_bike = nx.read_edgelist("data/Detroit/simple/Detroit_bike_simple.txt", nodetype=int)
graph_list.append(Detroit_bike)
Detroit_drive = nx.read_edgelist("data/Detroit/simple/Detroit_drive_simple.txt", nodetype=int)
graph_list.append(Detroit_drive)
Detroit_pedestrian = nx.read_edgelist("data/Detroit/simple/Detroit_walk_simple.txt", nodetype=int)
graph_list.append(Detroit_pedestrian)
Detroit_rail = nx.read_edgelist("data/Detroit/simple/Detroit_rail_simple.txt", nodetype=int)
graph_list.append(Detroit_rail)

Jakarta_bike = nx.read_edgelist("data/Jakarta/simple/Jakarta_bike_simple.txt", nodetype=int)
graph_list.append(Jakarta_bike)
Jakarta_drive = nx.read_edgelist("data/Jakarta/simple/Jakarta_drive_simple.txt", nodetype=int)
graph_list.append(Jakarta_drive)
Jakarta_pedestrian = nx.read_edgelist("data/Jakarta/simple/Jakarta_walk_simple.txt", nodetype=int)
graph_list.append(Jakarta_pedestrian)
Jakarta_rail = nx.read_edgelist("data/Jakarta/simple/Jakarta_rail_simple.txt", nodetype=int)
graph_list.append(Jakarta_rail)

LA_bike = nx.read_edgelist("data/LA/simple/LA_bike_simple.txt", nodetype=int)
graph_list.append(LA_bike)
LA_drive = nx.read_edgelist("data/LA/simple/LA_drive_simple.txt", nodetype=int)
graph_list.append(LA_drive)
LA_pedestrian = nx.read_edgelist("data/LA/simple/LA_walk_simple.txt", nodetype=int)
graph_list.append(LA_pedestrian)
LA_rail = nx.read_edgelist("data/LA/simple/LA_rail_simple.txt", nodetype=int)
graph_list.append(LA_rail)

London_bike = nx.read_edgelist("data/London/simple/London_bike_simple.txt", nodetype=int)
graph_list.append(London_bike)
London_drive = nx.read_edgelist("data/London/simple/London_drive_simple.txt", nodetype=int)
graph_list.append(London_drive)
London_pedestrian = nx.read_edgelist("data/London/simple/London_walk_simple.txt", nodetype=int)
graph_list.append(London_pedestrian)
London_rail = nx.read_edgelist("data/London/simple/London_rail_simple.txt", nodetype=int)
graph_list.append(London_rail)

Manhattan_bike = nx.read_edgelist("data/Manhattan/simple/Manhattan_bike_simple.txt", nodetype=int)
graph_list.append(Manhattan_bike)
Manhattan_drive = nx.read_edgelist("data/Manhattan/simple/Manhattan_drive_simple.txt", nodetype=int)
graph_list.append(Manhattan_drive)
Manhattan_pedestrian = nx.read_edgelist("data/Manhattan/simple/Manhattan_walk_simple.txt", nodetype=int)
graph_list.append(Manhattan_pedestrian)
Manhattan_rail = nx.read_edgelist("data/Manhattan/simple/Manhattan_rail_simple.txt", nodetype=int)
graph_list.append(Manhattan_rail)

Mexico_bike = nx.read_edgelist("data/Mexico/simple/Mexico_bike_simple.txt", nodetype=int)
graph_list.append(Mexico_bike)
Mexico_drive = nx.read_edgelist("data/Mexico/simple/Mexico_drive_simple.txt", nodetype=int)
graph_list.append(Mexico_drive)
Mexico_pedestrian = nx.read_edgelist("data/Mexico/simple/Mexico_walk_simple.txt", nodetype=int)
graph_list.append(Mexico_pedestrian)
Mexico_rail = nx.read_edgelist("data/Mexico/simple/Mexico_rail_simple.txt", nodetype=int)
graph_list.append(Mexico_rail)

Phoenix_bike = nx.read_edgelist("data/Phoenix/simple/Phoenix_bike_simple.txt", nodetype=int)
graph_list.append(Phoenix_bike)
Phoenix_drive = nx.read_edgelist("data/Phoenix/simple/Phoenix_drive_simple.txt", nodetype=int)
graph_list.append(Phoenix_drive)
Phoenix_pedestrian = nx.read_edgelist("data/Phoenix/simple/Phoenix_walk_simple.txt", nodetype=int)
graph_list.append(Phoenix_pedestrian)
Phoenix_rail = nx.read_edgelist("data/Phoenix/simple/Phoenix_rail_simple.txt", nodetype=int)
graph_list.append(Phoenix_rail)

Portland_bike = nx.read_edgelist("data/Portland/simple/Portland_bike_simple.txt", nodetype=int)
graph_list.append(Portland_bike)
Portland_drive = nx.read_edgelist("data/Portland/simple/Portland_drive_simple.txt", nodetype=int)
graph_list.append(Portland_drive)
Portland_pedestrian = nx.read_edgelist("data/Portland/simple/Portland_walk_simple.txt", nodetype=int)
graph_list.append(Portland_pedestrian)
Portland_rail = nx.read_edgelist("data/Portland/simple/Portland_rail_simple.txt", nodetype=int)
graph_list.append(Portland_rail)

for graph in graph_list:
    soma = 0
    maxDegree = 0
    for x in graph.degree:
        if x[1] > maxDegree:
            maxDegree = x[1]
        soma = soma + x[1]
    if len(graph.degree) != 0:
        print(f"Nodes - {len(graph.nodes)} | Edges - {len(graph.edges)} | Average Degree - {soma/len(graph.nodes)}")
    else:
        print(f"Nodes - {len(graph.nodes)} | Edges - {len(graph.edges)} | Average Degree - 0.00 | Max Degree - 0")

