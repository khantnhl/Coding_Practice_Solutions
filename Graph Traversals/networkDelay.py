from collections import defaultdict
import heapq
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
    # build adjlist
    adjlist = defaultdict(list)
    for u,v,time in times:
        adjlist[u].append((v, time))

    # distance 
    distance = { v: float('inf') for v in range(1, n+1)}
    distance[k] = 0
    pq = [(0, k)]

    while(pq):
        curTime, curNode = heapq.heappop(pq)

        for newNode, wt in adjlist[curNode]:
            newtime = curTime + wt

            if(newtime < distance[newNode]):
                distance[newNode] = newtime
                heapq.heappush(pq, (newtime, newNode))

    maxT = float("inf")
    maxT = max(distance.values())
    
    if(maxT != float('inf')):
        return maxT
    else:
        return -1


"""
time : O((N+Edges) * log Vertices)
space: O(N)
"""