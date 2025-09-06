import heapq
class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    # O(log N) time
    def addNum(self, num: int) -> None:
        # we want all elements in maxHeap to be smaller than elements in minHeap
        heapq.heappush(self.maxHeap, - num)
        heapq.heappush(self.minHeap, - heapq.heappop(self.maxHeap))

        if(len(self.maxHeap) < len(self.minHeap)):
            heapq.heappush(self.maxHeap, - heapq.heappop(self.minHeap))

    # O(1) time 
    def findMedian(self) -> float:
        # if we have odd-length array, top of maxHeap is the answer
        if(len(self.maxHeap) > len(self.minHeap)):
            return - self.maxHeap[0]
        
        # else we take top of each and averaged
        return  (- self.maxHeap[0] + self.minHeap[0])/2

    # space O(N)
