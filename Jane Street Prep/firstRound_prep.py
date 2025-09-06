# ALL OF THESE QUESTIONS/ANSWERS ARE MADE UP BY ME WITH HELP FROM LLMS 
# TO HELP ME PRACTICE NOT REAL INTERVIEW QUESTIONS

"""
Suppose you need to process 1 billion trades per day. 
How would you design a system to: 
    Keep track of the top 10 trades by volume 
    Guarantee low memory usage and constant-time updates

Input example : 
{
    trade_id     : unique identifier
    timestamp    : time trade executed
    symbol       : stock/asset symbol (e.g., AAPL)
    volume       : number of shares/contracts traded
    price        : trade price
    side         : buy/sell
}

IDEA: store (volume, id) tuple in minHeap
      store only 10 largest trades
"""
import heapq
def trade(trades):
    minHeap = []
    for trade in trades:
        if(len(minHeap) < 10):
            heapq.heappush(minHeap, (trade.volume, trade.trade_id))
        else:
            # only if incoming is bigger
            if(trade.volume > minHeap[0][0]):
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, (trade.volume, trade.trade_id))
    return minHeap

"""
Given a stream of integers, design a data structure to:
Insert numbers
Return the median at any time
(Discuss trade-offs, not just code)

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

IDEA: 
We can use Balanced BST with O(logn) time insertion. But more complex to implement. 
Optimal: We can use min-max Heaps and return the top of the heap 
"""
class Median():
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    
    # all elements in maxHeap has to be less than those in the minHeap
    def addNum(self, num : int):
        heapq.heappush(self.maxHeap, - num) # negate values for maxHeap
        heapq.heappush(self.minHeap, - heapq.heappop(self.maxHeap)) 

        if(len(self.maxHeap) < len(self.minHeap)):
            heapq.heappush(self.maxHeap, - heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if(len(self.maxHeap) > len(self.minHeap)):
            return - self.maxHeap[0]

        return (- self.maxHeap[0] + self.minHeap[0])/2

"""
In C, what happens if two threads write to the same memory location without synchronization?
Ans: data race condition where behavior is undefined. Final value is not defined and we need explicit synchronization to fix. 
"""

"""
Design an orderbook system from scratch, 
what would these APIs look like?
    - addOrder
    - cancelOrder
    - updateOrder
    - getBestBid
    - getBestAsk
    - getDepth
    - matchOrder 
"""

"""
Given a basic API for a low‑level disk drive, 
implement a file system that can read and write.
"""

"""
build an interpreter for a simple programming language
"""

"""
Implement a function that, given a list of integers, 
returns all pairs of numbers that sum to zero
"""

"""
Design Tetris
"""

"""
Design a video player API
"""

"""
Implement a chess game and discuss the design choices
"""

"""
Write an AI bot for a simple game scenario.
"""

"""
build an interpreter for a simple programming language, 
"""

"""
Creating a mini debugger for some made-up language
"""