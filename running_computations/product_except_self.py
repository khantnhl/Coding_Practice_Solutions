from typing import List

"""
time : O(n)
space: O(n)
"""
def productExceptSelf(nums: List[int]) -> List[int]:
    # [1,2,4,6]

    # prefix prod
    # [1, 1*1]
    # [1, 1, 1*2]
    # [1,1,2,2*4]

    # suffix prod
    # [1,1,2,8]
    # [1*(24*2),1*(6*4),2*(1*6),8*1]

    result = [1] * len(nums)

    # left to right, product before left pointer
    for i in range(1, len(nums)):
        result[i] = result[i-1] * nums[i-1]

    print(result)
    suffix = 1
    # product after right pointer
    for i in range(len(nums)-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
        print(suffix)

    return result