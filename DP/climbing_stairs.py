# count ways to reach top of stairs
"""
Brute force recursion 
    time : O(2^n) 
    space: O(n)
Optimal
    time : O(n)
    space: O(n)
0 stair -> 1 way which is do nothing
1 stair -> 1 way
"""
def countWays(n):
    dp = [0] * (n + 1)

    # Base
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# count ways to reach n-th stair
# can take 1, 2, or 3 steps

def countWays(n):
    #base 
    if(n==0 or n==1): 
        return 1
    if(n==2):
        return 2
    
    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


