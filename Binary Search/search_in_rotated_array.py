"""
    search range method 
    time: O(log n)
    space: O(1)
"""

def search(self, nums: List[int], target: int) -> int:
    
    left, right = 0, len(nums)-1

    while(left <= right):

        mid = (left + right) // 2

        if(nums[mid]==target):
            return mid

        if(nums[mid] <= nums[right]):
            if(target < nums[mid] or target > nums[right]):
                right = mid - 1
            else:
                left = mid + 1
        else:
            if(target > nums[mid] or target < nums[left]):
                left = mid + 1
            else:
                right = mid - 1

    return -1
