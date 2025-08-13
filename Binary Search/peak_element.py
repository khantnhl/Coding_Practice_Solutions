
def findPeakElement(self, nums: List[int]) -> int:
    left, right = 0, len(nums)-1
    # [1,2,1,3,5,6,4]
    #  l.    m c   r
    #          l m r     
    # 
    while(left < right):
        mid = (left + right)//2
        if(nums[mid] < nums[mid + 1]):
            left = mid + 1
        else:
            right = mid
    
    return left