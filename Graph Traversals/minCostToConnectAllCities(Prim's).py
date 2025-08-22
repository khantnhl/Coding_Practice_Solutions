"""
    0    1      2     3     4
[[0,0],[2,2],[3,10],[5,2],[7,0]]

Prim's Algorithm - visit all nodes
time : O(n^2 log n) 
space: O(n)
"""

from typing import List
import heapq
def minCostConnectPoints(self, points: List[List[int]]) -> int:
    visited = set()
    minHeap = [(0, 0)]
    nodes = len(points)
    adjlist = { v:[] for v in range(nodes)}

    for i in range(len(points)):
        x1, y1 = points[i]
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            dist = abs(x1-x2) + abs(y1-y2)
            adjlist[i].append([dist, j])
            adjlist[j].append([dist, i])

    result = 0
    while(len(visited) < nodes):
        curCost, curNode = heapq.heappop(minHeap)

        if(curNode in visited): continue

        result += curCost
        visited.add(curNode)

        for wt, nei in adjlist[curNode]:
            if(nei not in visited):
                heapq.heappush(minHeap, [wt, nei])

    return result