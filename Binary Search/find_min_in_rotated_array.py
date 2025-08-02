"""
    lower bound search method
    time : O(log n)
    space: O(1)
"""

def findMin(self, nums: List[int]) -> int:
# [3,4,5,6,1,2]
#  l     m   r
#          l r   
    left, right = 0, len(nums)-1
    result = 0
    while(left < right):
        
        mid = (left + right)//2

        if(nums[mid] < nums[right]):
            right = mid 
        else:
            left = mid + 1

    return nums[left]