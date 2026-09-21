import networkx as nx
import matplotlib.pyplot as plt
from analyzer.extrator import DataExtractor

with open("zelda1.nes", "rb") as f:
    d = DataExtractor(f)
    d.Parse()

    for level in range(1,10):
        G = nx.Graph()
        node_color_list = []
        edge_color_list = []
        for room in d.data[level].values():
            # print(room)
            coord = (room['col'],room['row'])
            node_color = "blue"
            if room["item_info"] == "D Key" or room["item_info"] == "Key":
                node_color = "orange"
            G.add_node(coord,pos=coord,east=room["east.wall_type"],north=room["north.wall_type"])
            node_color_list += [node_color]
        for v in G.nodes():
            DOORS = ["Door", "Locked Door", "Shutter Door", "Bomb Hole"]
            if G.nodes[v]["east"] in DOORS:
                color = "black"
                if G.nodes[v]["east"] == "Locked Door":
                    color = "red"
                G.add_edge(v,(v[0]+1,v[1]))
                edge_color_list += [color]
            if G.nodes[v]["north"] in DOORS:
                color = "black"
                if G.nodes[v]["north"] == "Locked Door":
                    color = "red"
                G.add_edge(v,(v[0],v[1]+1))
                edge_color_list += [color]
        nx.draw(G,pos={v:v for v in G.nodes()}, node_color=node_color_list, edge_color=edge_color_list)
        plt.savefig(f"level{level}.png", format="PNG")
        plt.clf()

    

    # TODO: convert each level of Zelda1 into a networkx graph object:
    # import networkx as nx
    # G = nx.Graph()
