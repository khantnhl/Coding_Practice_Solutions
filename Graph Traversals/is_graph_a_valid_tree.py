"""
    time : O(v + e)
    space: O(v + e)
"""

from collections import List

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

