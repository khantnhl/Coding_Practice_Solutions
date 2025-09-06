"""

no two adjacent houses

"""
class Solution:
    def rob(self, nums) -> int:
        
        # first element, without first element, without last element
        return max(nums[0], self.helper(nums[1: ]), self.helper(nums[ :-1]))

    def helper(self, arr):
            rob1, rob2 = 0, 0

            for num in arr:
                hold = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = hold

            return rob2

# Instead of creating copys of arrays
# pass in start and end index
# time : O(N)
# space: O(1)
class Solution:
    def rob(self, nums) -> int:
        return max(nums[0], self.helper(nums, 1, len(nums)-1), self.helper(nums, 0, len(nums)-2))

    def helper(self, nums, start, end):

        rob1, rob2 = 0, 0

        for i in range(start, end + 1):
            hold = max(nums[i] + rob1, rob2)
            rob1 = rob2 
            rob2 = hold
        
        return rob2

"""
how this works:

[2,9,8,3,6], Output: 15
   l.    l
 r     r
max(2, helper(1, 4), helper(0, 3))
helper(1, 4) returns 
    0, 0  [9,8,3,6], hold = 2 + 0
    r1 r2  h

"""