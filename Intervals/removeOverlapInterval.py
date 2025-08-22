def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    
    intervals.sort(key = lambda x : x[1])
    prevEnd = intervals[0][1]
    result = 0
    for start, end in intervals[1:]:
        if(prevEnd <= start):
            # no overlap
            prevEnd = end
        else:
            result += 1

    return result

