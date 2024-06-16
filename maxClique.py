from graph import Graph
from os import sys



def bron_kerbosch(R, P, X, graph, cliques):
    if not P and not X:
        cliques.append(R)
        return
    
    while P:
        v = P.pop()
        new_R = R + [v]
        new_P = [vertex for vertex in P if vertex in graph[v]]
        new_X = [vertex for vertex in X if vertex in graph[v]]
        bron_kerbosch(new_R, new_P, new_X, graph, cliques)
        X.append(v)
