"""
time : O(NlogN)
space: O(1)

    [-1,0,1,2,-1,-4]
    [-4,-1,-1,0,1,2]
        i   j        k


    [-2,0,0,2,2]
        i j     k
        i   j k  
"""
def threeSum(self, nums: List[int]) -> List[List[int]]: 
    nums.sort() # O(NlogN)
    result = []

    for i in range(len(nums)):
        if(i > 0 and nums[i]==nums[i-1]):
            continue

        j = i+1
        k = len(nums)-1
        
        while(j < k):

            curSum = nums[i] + nums[j] + nums[k]

            if(curSum == 0):
                result.append([nums[i],nums[j],nums[k]])

                j += 1
                k -= 1

                while(j < k and nums[j]==nums[j-1]):
                    j += 1
                while(k > j and nums[k]==nums[k+1]):
                    k -= 1

            elif(curSum < 0):
                j += 1
            else:
                k -= 1
    return result