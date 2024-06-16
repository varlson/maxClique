from os import sys
from graph import Graph
from maxClique import bron_kerbosch

def loadGraphInfo(filename):
    edges = []
    N = 0
    with open(filename, 'r') as file:
        for line in file:
            if line[0] == 'e':
                u, v = int(line.split(' ')[1]),int(line.split(' ')[2])
                edges.append((u, v))
            if line[0] == 'p':
                N = int(line.split(' ')[2])
    return N, edges


def loadGraph(N, edges):
    g = Graph(N)
    for u, v in edges:
        g.add_edge(v, u)
        g.add_edge(u, v)
    return g

def main(filename):
    N, edges = loadGraphInfo(filename)
    graph = loadGraph(N, edges)
    cliques = []
    vertices = list(graph.keys())
    bron_kerbosch([], vertices, [], graph, cliques)
    index = max([len(x)] for x in cliques)
    print("Cliques encontrados:", index)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Forneça caminho completo do ficheiro")
        sys.exit()
    else:
        filePath = sys.argv[1]
        main(filePath)
   