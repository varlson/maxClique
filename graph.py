class Graph:
    def __init__(self, size):
        self.g = {}
        for node in range(1, size+1):
            self.g[node] = set()

    def add_edge(self, u, v):
        self.g[u] = set(list(self.g[u])+ [v])
        self.g[v] = set(list(self.g[v])+ [u])
    
    def keys(self):
        return set(self.g.keys())

    def __getitem__(sel, key):
        return sel.g.get(key)
    


