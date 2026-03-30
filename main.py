import networkx as nx
from analyzer.extrator import DataExtractor

with open("zelda1.nes", "rb") as f:
    d = DataExtractor(f)
    print(d.level_info)

    # TODO: convert each level of Zelda1 into a networkx graph object:
    # import networkx as nx
    # G = nx.Graph()
