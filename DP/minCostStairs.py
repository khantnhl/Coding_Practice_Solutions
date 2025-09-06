# 
# cost = [1,2,3], output = 2
# can step to either the (i + 1)th floor or the (i + 2)th floor.
# may start at index 0 or 1 
# return min cost to reach top

# RECURSION METHOD
def minCostClimbingStairs(self, cost) -> int:   

    n = len(cost)

    def recur(i):
        
        if(i==0 or i==1):
            return cost[i]

        return cost[i] + min(recur(i - 1), recur(i - 2))
    
    return min(recur(n-1), recur(n-2))

# TABULATION
def minCostClimbingStairs(self, cost) -> int:   
    n = len(cost)
    dp = [0] * (n)
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(cost[i - 1], cost[i - 2])
    
    return min(dp[n - 1], dp[n - 2])

# OPTIMIZED SPACE 
# cost = [1, 2, 3, 4, 5]
#            <- i
#        [7, 6, 7, 4, 5]
#       ans ans 
def minCostClimbingStairs(self, cost) -> int:
    # iterate backwards
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])
    
    return min(cost[0], cost[1])