# Given an origin and a destination in a directed graph in which edges can be blue or red, 
# determine the length of the shortest path from the origin to the destination in which the edges traversed alternate in color. 
# Return -1 if no such path exists.

# Examples:
# [(A, B, "blue"), (A, C, "red"), (B, D, "blue"), (B, E, "blue"), (C, B, "red"), (D, C, "blue"), (A, D, "red"), (D, E, "red"), (E, C, "red")]

# Input: origin = A, destination = E
# Output: 4 (path: A→D (red), D→C (blue), C→B (red), B→E (blue))

from collections import deque, defaultdict

def alternatingPath(edges : list, src : str, dest : str):

    adjlist = defaultdict(list)

    for u,v,color in edges:            
        adjlist[u].append((v, color))

    queue = deque([(src, None, 0)])
    visited = set()

    while(queue):
        cur, prevColor, track = queue.popleft()

        visited.add((cur, prevColor))

        if(cur == dest):
            return track

        if(cur not in adjlist):
            continue
        
        for neighbor, Curcolor in adjlist[cur]:
            if(prevColor != Curcolor and (neighbor, Curcolor) not in visited):
                queue.append((neighbor, Curcolor, track + 1))

    return -1

# print(alternatingPath([('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"), ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")], 'A', 'E'))
