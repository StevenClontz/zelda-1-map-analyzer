import networkx as nx
import matplotlib.pyplot as plt
from analyzer.extrator import DataExtractor

with open("zelda1.nes", "rb") as f:
    d = DataExtractor(f)
    d.Parse()

    for level in range(1,10):
        G = nx.Graph()
        for room in d.data[level].values():
            coord = (room['col'],room['row'])
            G.add_node(coord,pos=coord,east=room["east.wall_type"],north=room["north.wall_type"])
        for v in G.nodes():
            DOORS = ["Door", "Locked Door", "Shutter Door", "Bomb Hole"]
            if G.nodes[v]["east"] in DOORS:
                G.add_edge(v,(v[0]+1,v[1]))
            if G.nodes[v]["north"] in DOORS:
                G.add_edge(v,(v[0],v[1]+1))
        nx.draw(G,pos={v:v for v in G.nodes()})
        plt.savefig(f"level{level}.png", format="PNG")
        plt.clf()

    

    # TODO: convert each level of Zelda1 into a networkx graph object:
    # import networkx as nx
    # G = nx.Graph()
