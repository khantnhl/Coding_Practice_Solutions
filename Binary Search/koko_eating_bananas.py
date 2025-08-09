"""
time: O(n log m)
space: O(1)
"""

def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
    # [1,4,3,2], h=9
    # max(piles) = 4
    # 0 1 2 3 4
    # l.  m   r
    # [1,4,3,2]
    #. 1/2=1, 4/2=2, 3/2=2, 2/2=1 -> 6

    # 1/1=1, 4/1=4, 3/1=3, 2/1=2 -> 10
    # time_taken = math.cel(pile / mid) for each pile
    # if totak time_taken is <= h
    # save the answer and find on left half

    left, right = 1, max(piles)

    while(left <= right):

        mid = (left + right) // 2

        time_taken = 0 
        for pile in piles:
            time_taken += math.ceil(pile/mid)

        if(time_taken <= h):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans
