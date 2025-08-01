"""
time : O(n)
space: O(n) for Set 
idea : iterate over the set to avoid duplicates and keep looking for num - 1
""" 
def longestConsecutive(self, nums: List[int]) -> int:
    if(not nums):
        return 0
    uniqueSet = set(nums)
    maxl = 1
    for num in nums:
        track = 1
        while(num - 1 in uniqueSet):
            track += 1
            num -= 1
        maxl = max(maxl, track)

    return maxl
