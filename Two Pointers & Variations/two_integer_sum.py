"""
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
There will always be exactly one valid solution.
Your solution must use O(1) additional space.
How can you take advantage of array being sorted? 
must answer in O(1) space so no Hashmap is allowed.
"""

def twoSumII(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers)-1

    while(left < right):

        curSum = numbers[left] + numbers[right]

        if(curSum == target):
            return [left+1, right+1]
        elif(curSum < target):
            left += 1
        else:
            right -= 1
            