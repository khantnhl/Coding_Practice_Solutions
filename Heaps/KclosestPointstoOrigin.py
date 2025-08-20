import heapq, math

"""
time : O(n log k)
space: O(n)
"""
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

    maxHeap = []
    for x, y in points:
        dist = - math.sqrt(x**2 + y**2) # maxHeap
        
        if(len(maxHeap) == k):
            heapq.heappushpop(maxHeap, (dist, x, y))
        else:
            heapq.heappush(maxHeap, (dist, x, y))
    
    return [(x,y) for (dist,x,y) in maxHeap]