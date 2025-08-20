"""
    time : O(v + e)
    space: O(v + e)
"""

from collections import List

# DFS Approach
def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
    from collections import defaultdict
    visited = set()

    # build adjlist
    adjlist = defaultdict(list)
    for u, v in edges:
        adjlist[u].append(v)
        adjlist[v].append(u)

    # use DFS
    def dfs(node, parent):
        # if already visited, there is cycle!
        if(node in visited):
            return False

        visited.add(node)

        for neighbor in adjlist[node]:
            # stepping over same node from different path -> skip 
            if(neighbor == parent): 
                continue 

            if(not dfs(neighbor, node)):
                return False
        
        return True

    return dfs(0, -1) and len(visited)==n


# BFS Approach
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    # convert to adjlist
    from collections import defaultdict, deque
    adjlist = defaultdict(list)
    for u, v in edges:
        adjlist[u].append(v)
        adjlist[v].append(u)

    # BFS
    visited = set()
    # [(node, parent)]
    queue = deque([(0,-1)])
    # current node, parent

    visited.add(0)
    while(queue):
        node, parent = queue.popleft()

        for neighbor in adjlist[node]:
            
            if(neighbor == parent):
                continue
            if(neighbor in visited):
                return False

            visited.add(neighbor)
            queue.append((neighbor, node))

    return len(visited)==n

