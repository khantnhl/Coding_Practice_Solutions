# Given a list of towns and a list of pairs representing roads between towns, 
# return the number of road networks.

# Examples:
# Input: ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"], 
# [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]

from collections import defaultdict, deque
def roadNetworks(towns : list , edges : list) -> int : 

    visited = set()
    adjlist = defaultdict(list)
    numroads = 0

    # build adjlist (undirected graph)
    for u,v in edges:
        adjlist[u].append(v)
        adjlist[v].append(u)

    for town in adjlist:
        if(town not in visited):
            queue = deque([town])
            visited.add(town)

            while(queue):
                curTown = queue.popleft()

                for neighbor in adjlist[curTown]:
                    if(neighbor not in visited):
                        queue.append(neighbor)
                        visited.add(neighbor)
            numroads+=1
    return numroads


print(roadNetworks(["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"], 
                   [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]))

