"""
time : O(logN)
space: O(1)
"""
def minimumTime(self, time: List[int], totalTrips: int) -> int:
    """
    time=[1,2,3]
    [1,0,0] busA 1,2,3,4,5...
    [2,1,0] busB 2,4,6,8,..
    [3,1,1] busC 3,6,9,..

    l=1, r=1*5
    m=3, [3//1, 3//2, 3//3]->[3,1,1]-> 5 >= 5
    """
    l = 1
    r = min(time) * totalTrips 

    while(l < r):
        mid = (l + r) // 2

        if(sum(mid // t for t in time) >= totalTrips):
            r = mid # becuz we want to find minimum time
        else:
            l = mid + 1

    return l
