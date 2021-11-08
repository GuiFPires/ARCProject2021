# ARCProject2021

ARC Project

Studying Urban Transportation Networks Usinga Multi-Layered Approach (paper in the project's directory)

Group 7
98722	Miguel Rodrigo da Costa Figueiredo
102124	Daniel António Graça Dias
102132	Guilherme França Pereira de Almeida Pires


Before executing:

The project is made in python so you need to have python installed on your computer. We also use some specific libraries:networkx, matplotlib, altair and pandas, so
you will need to install  them by running these python commands:

pip install networkx[default]
pip install -U matplotlib
pip install -U altair
pip install altair_viewer
pip install pandas

Project overview:

Folders:

data folder - contains every city's network data, as well as two Json files: cities_data.json that has each city's Bike, Rail, Pedestrian, Drive and Multi-layered networks data as well as its population and overlap_data.json that has each city's Congestion Level(in percentage), pedestrian-drive network overlap census, and group(considering its overall analysis of the overlap census done on the paper, referred on 3.1).

results folder - contains every graph presented by us in the paper: Figure1.png represents the histogram regarding the degree distribution example(on paper's point 2); every png named after a city represents their overlap census graphs(represented on 3.2); Nodes_Population.png and Links_Population.png represent the linear regressions done on 3.2 and Ranking_Regression.png that represents the linear regression done on 4.1.2. as well as three txt files: first_table.txt that contains the data used to fill the first table in the paper; second_table.txt that contains the data used to fill the second table in the paper and pedestrian_drive_oc.txt that contain the cities' pedestrian-drive network overlap census used to fill up data/overlap_data.json



Python files(to run them, make sure you are on the project directory - using cd project path (Eg.: cd G:\IST\CRC\Projeto)):

degree_dist_example.py - generates the histogram regarding the degree distribution example(on paper's point 2), to run this script simply do:
	python degree_dist_example.py
	then you can save the image, the window that shows up has a save button and you can save it directly to where you want it to be(in our case - results/Figure1.png)

first_table.py - prints the data of each city's(ordered alphabetically) networks, used to write the first table on the paper, we directed the output to a file, so to run this script do:
	python first_table.py > results/first_table.txt (it can be other file or directory this is just the one we used and where you will find the results)

second_table.py - creates each city's multi-layered network and writes their data to a file(results/second_table.txt) - used to write the first table on the paper - to run this script simply do:
	python second_table.py

overlap_census.py - generates each city's overlap census graph - used in our paper's 3.1 section - it has three functions(overlap_networks, overlap_degree_vectors and overlap_census) written by the people who made the paper(https://findingspress.org/article/13171-extracting-the-multimodal-fingerprint-of-urban-transportation-networks) that inspired ours, you can find their full code on: https://github.com/nateraluis/Multimodal-Fingerprint
		 to run this script simply do:
		python overlap_census.py
		then you can save every graph, the window that shows up has a save button and you can save it directly to where you want it to be(in our case the graphs ar in the results folder)

population_nodes.py - generates the plot relating each city's networks nodes and its population used in our paper's 3.2 section, to run this script simply do:
		python population_nodes.py
		a localhost webpage will pop up with a interactive graph where you can download the image(in our case the image is results/Nodes_Population.png)

population_links.py - generates the plot relating each city's networks edges and its population used in our paper's 3.2 section, to run this script simply do:
		python population_links.py
		a localhost webpage will pop up with a interactive graph where you can download the image(in our case the image is results/Links_Population.png)

get_population_drive_oc.py - prints each city's Pedestrian-Drive network overlap census, used to fill up the data in data/overlap_data.json that will be used to plot the graph 4.1.2 - it has three functions(overlap_networks, overlap_degree_vectors and overlap_census) written by the people who made the paper(https://findingspress.org/article/13171-extracting-the-multimodal-fingerprint-of-urban-transportation-networks) that inspired ours, you can find their full code on: https://github.com/nateraluis/Multimodal-Fingerprint , we directed the output to a file, so to run this script do:
		
    python get_population_drive_oc.py > results/pedestrian_drive_oc.txt (it can be other file or directory this is just the one we used and where you will find the results)

ranking_conclusions- generates the plot relating each city's traffic congestion level and its pedestrian-drive network overlap census, used in our paper's 4.1.2 section, to run this script simply do:
		python ranking_conclusions.py
		a localhost webpage will pop up with a interactive graph where you can download the image(in our case the image is results/Ranking_Regression.png)


Urban_Transportation_Networks_Multi-Layered_Approach.pdf - Our final paper.
