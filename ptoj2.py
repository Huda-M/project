class Kruskal:
    def __init__(self, vertices):
        self.vertices = vertices  
        self.edges = []  
    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))    
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))  
            self.rank = [0] * n  
        def find(self, u):
            if self.parent[u] != u:
                self.parent[u] = self.find(self.parent[u])  
            return self.parent[u]
        def union(self, u, v):
            root_u = self.find(u)
            root_v = self.find(v)
            if root_u != root_v:
                if self.rank[root_u] > self.rank[root_v]:
                    self.parent[root_v] = root_u
                elif self.rank[root_u] < self.rank[root_v]:
                    self.parent[root_u] = root_v
                else:
                    self.parent[root_v] = root_u
                    self.rank[root_u] += 1
    def kruskal(self):
        self.edges.sort()  
        uf = self.UnionFind(self.vertices)
        mst = []  
        mst_weight = 0  
        for weight, u, v in self.edges:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)  
                mst.append((u, v, weight)) 
                mst_weight += weight  
        return mst, mst_weight 

g = Kruskal(4)
g.add_edge(0, 1, 10)  
g.add_edge(0, 2, 6)  
g.add_edge(0, 3, 5)   
g.add_edge(1, 3, 15)  
g.add_edge(2, 3, 4)   
mst, mst_weight = g.kruskal() 
print("Edges in the Minimum Spanning Tree (MST):", mst)
print("Total weight of the MST:", mst_weight)
