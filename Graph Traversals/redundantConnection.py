# given a connected undirected graph with 1 to n nodes
# Return an edge that can be removed so that the graph is still a connected non-cyclical graph.
# edges = [[1,2],[1,3],[3,4],[2,4]]
# ans [2,4]
"""
1-> 2 -> 4
1-> 3 -> 4

time : O(v + e)
space: O(v + e)

can be solved with Union Find and TopoSort Kahn's algorithm
"""
from typing import List
from collections import defaultdict
def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    
    adjlist = defaultdict(list)
    for u,v in edges:
        adjlist[u].append(v)
        adjlist[v].append(u)

    visited = set()
    cycle = set()
    cycleStart = -1

    def dfs(node, parent):
        nonlocal cycleStart

        # Base Case: detected cycle by revisiting
        if(node in visited):
            cycleStart = node
            return True
        
        visited.add(node)
        for neighbor in adjlist[node]:
            # back edge path
            if(neighbor == parent):
                continue
            
            if(dfs(neighbor, node)):
                # backward after recursion
                if(cycleStart != -1):
                    cycle.add(node)

                # if it is the start of cycle, reset 
                if(node == cycleStart):
                    cycleStart = -1
                return True
        return False

    dfs(1, -1) 
    
    # find edge backwards
    for u, v in reversed(edges):
        if(u in cycle and v in cycle):
            return [u,v]

    return []


# Union-Find
def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    parent = [i for i in range(len(edges)+1)]
    rank = [1] * (len(edges)+1)

    def find(n):
        if(n != parent[n]):
            parent[n] = find(parent[n])
        return parent[n]

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if(p1 == p2):
            return False

        if(rank[p1] > rank[p2]):
            parent[p2] = p1
            rank[p1] += rank[p2]
        else:
            parent[p1] = p2
            rank[p2] += rank[p1]
        
        return True

    for n1, n2 in edges:
        if(not union(n1, n2)):
            return [n1, n2]