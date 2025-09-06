"""
    rob i and i + 2 or rob i + 1

"""

def rob(self, nums) -> int:
    def recur(nums, idx):

        if(idx >= len(nums)):
            return 0
        
        return max(recur(nums, idx+1), nums[idx] + recur(nums, idx+2))

    return recur(nums, 0)

# Tabulation O(N) time
def rob(self, nums) -> int:

    dp = [0] * (len(nums) + 1)
    #[0,0,0,0, 0,0]
    #  [5,3,4,11,2]

    dp[0] = 0
    dp[1] = nums[0]

    for i in range(2, len(nums)+1):
        dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])

    return dp[len(nums)]


"""
        [5, 3, 4, 11, 2]
r1, r2
hold = 5 + 0
        [5, 3, 4, 11, 2]

"""
    
# Space Optimized O(1)
def rob(self, nums) -> int:

    rob1, rob2 = 0, 0

    for num in nums:
        hold = max(num + rob2, rob1)

        rob2 = rob1
        rob1 = hold

    return rob1