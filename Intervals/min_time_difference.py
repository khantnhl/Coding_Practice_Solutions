def findMinDifference(self, timePoints: List[str]) -> int:
        
    # convert to minutes 
    # if there are more points than minutes in a day, diff is gonna be 0
    # sort the timepoints
    # handle circular time points
    
    if(len(timePoints) > 24 * 60): return 0

    sorted_points = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)

    sorted_points.append(sorted_points[0] + 24 * 60) # first elem to end of list for circular difference

    min_diff = sorted_points[-1] # start comparing with biggest value
    
    for i in range(1, len(sorted_points)):
        min_diff = min(min_diff, sorted_points[i] - sorted_points[i-1])
    
    return min_diff