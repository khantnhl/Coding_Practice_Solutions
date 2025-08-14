# time : O(n log k)

import heapq
def mergeKsortedArray(arr : list[list[int]], k : int) -> list:

    minHeap = []
    result = []

    for i in range(len(arr)):
        if(arr[i]):
            heapq.heappush(minHeap, (arr[i][0], 0, 0))
    
    while(minHeap):
        val, arr_idx, elem_idx = heapq.heappop()
        result.append(val)

        if(elem_idx + 1 < len(arr[arr_idx])):
            nextVal = arr[arr_idx + 1]
            heapq.heappush(minHeap, (nextVal, arr_idx+1, elem_idx+1))

    return result