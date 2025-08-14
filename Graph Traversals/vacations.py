# Given an origin city, a maximum travel time k, 
# and pairs of destinations that can be reached directly from each other with corresponding travel times in hours, 
# return the number of destinations within k hours of the origin. 
# Assume that having a stopover in a city adds an hour of travel time.

# Examples:
# Input: [("Boston", "New York", 4), ("New York", "Philadelphia.", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]

# Origin = "New York", k=5
# Output: 2 (["Boston", "Philadelphia"])

import heapq
def vacationDestinations(edges : list, src : str, k : int):
    
    from collections import defaultdict
    adjlist=defaultdict(list)
    # build adjlist 
    for u,v,time in edges:
        adjlist[u].append((v, time))
        adjlist[v].append((u,time))

    minheap = []
    heapq.heappush(minheap, (src, 0))
    # curCity, time, 
    visited = set()
    destionations = []

    while(minheap):
        curCity, time = heapq.heappop(minheap)

        if(curCity in visited): continue

        visited.add(src)

        # within k hours
        if(curCity != src and time <= k):
            destionations.append(curCity)

        for neighbor, nexttime in adjlist[curCity]:
            stopover = 1 if(curCity == neighbor) else 0
            total = time + nexttime + stopover
            
            # within k hours
            if(total <= k):
                heapq.heappush(minheap, (neighbor, total))


    return destionations    

print(vacationDestinations([("Boston", "New York", 4), ("New York", "Philadelphia.", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)],"New York", k=5))
