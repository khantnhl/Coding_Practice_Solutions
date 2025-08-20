from typing import List

def countComponents(self, n: int, edges: List[List[int]]) -> int:  
    
    from collections import defaultdict
    # idea: dfs call on each node 0 -> n-1
    visited = set()
    components = 0

    adjlist = defaultdict(list)
    for u, v in edges:
        adjlist[u].append(v)
        adjlist[v].append(u)

    def dfs(node):
        for nei in adjlist[node]:
            if(nei not in visited):
                visited.add(nei)
                dfs(nei)

    for i in range(n):
        if(i not in visited):
            visited.add(i)
            dfs(i)
            components += 1
    return components