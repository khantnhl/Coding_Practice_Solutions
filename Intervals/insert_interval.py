"""

"""

def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
    i=0
    result = []

    while(i < len(intervals) and newInterval[0] > intervals[i][1]):
        result.append(intervals[i])
        i += 1


    while(i < len(intervals) and newInterval[1] >= intervals[i][0]):
        newInterval[0] = min()
        newInterval[1] = max()
        i += 1

    while(i < len(intervals)):
        result.append(intervals[i])
        i += 1
    return result