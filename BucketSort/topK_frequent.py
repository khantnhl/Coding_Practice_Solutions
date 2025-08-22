from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    uses maxHeap
    time : O(nlogk) can be Optimized -> O(n) below
    space: O(n+k)
    """

    _freq = {}
    for num in nums:
        _freq[num] = _freq.get(num, 0) + 1

    # [1,2,2,3,3,3]
    maxHeap = [] # (3, 3), (2, 2), (1, 1)
    import heapq
    for num in _freq.keys():
        heapq.heappush(maxHeap, (_freq[num], num))
        
        # hold at most k 
        if(len(maxHeap) > k):
            heapq.heappop(maxHeap)

    result = []
    for i in range(k):
        result.append(heapq.heappop(maxHeap))

    return result

def topKFrequent(nums: List[int], k: int) -> List[int]:        
    """
    uses Bucket Sort 
    time : O(n)
    space: O(n)
    
    [1,2,2,3,3,3]

    initialized to size of nums array to address max frequency 
    _freq = [ [], [], [], [], [], [], [] ]
    """

    # bucket sort
    _freq = {}
    for num in nums:
        _freq[num] = _freq.get(num,0) + 1

    from collections import defaultdict
    buckets = [[] for i in range(len(nums) + 1)]

    for key, freq in _freq.items():
        buckets[freq].append(key)

    result = []
                # start iteration from most frequent index bucket
    for i in range(len(buckets)-1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if(len(result) == k):
                return result