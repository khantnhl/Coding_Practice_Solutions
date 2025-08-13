
def threeSumClosest(self, nums: List[int], target: int) -> int:
        
    # use abs value to find closest value

    nums.sort()
    closestSum = float('inf')
    min_diff = float('inf')

    for i in range(len(nums)):
        left = i + 1
        right = len(nums)-1

        while(left < right):
            
            curSum = nums[i] + nums[left] + nums[right]
            curDiff = abs(curSum - target)

            if(curDiff < min_diff): # update
                min_diff = curDiff
                closestSum = curSum 

            if(curSum < target):
                left += 1
            else:
                right -= 1
    
    return closestSum
                

