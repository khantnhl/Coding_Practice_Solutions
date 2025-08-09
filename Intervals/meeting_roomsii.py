def minMeetingRooms(self, intervals: List[Interval]) -> int:
    """
    use minHeap and process the meeting end times
    if it ends early that means we can reuse the room
    else we cannot. need a new room. 
    """
    # (0,40),(5,10),(15,20)
    # minHeap [40]
    # minHeap push [10, 40]

    # (1,5),(2,6),(3,7),(4,8),(5,9)
    if not intervals:
        return 0

    import heapq
    minheap = []
    sorted_intervals = sorted(intervals, key=lambda x : x.start)

    heapq.heappush(minheap, sorted_intervals[0].end)
    
    # (0,40),(5,10),(15,20)
    # heap = 40 
    # 40 > 5
    # heap = 10
    # 10 < 15
    for i in range(1, len(sorted_intervals)):
        # if end time bigger than or equal to start time
        if(minheap[0] >= sorted_intervals[i].start):
            heapq.heappop(minheap)
        heapq.heappush(minheap, sorted_intervals[i].end)

    return len(minheap)
    