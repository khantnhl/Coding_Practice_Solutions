"""
coins = [1,5,10], amount = 12
ans = 3
"""

# RECURSION METHOD
# time O(2^N)
def coinChange(self, coins, amount: int) -> int:

    def reCur_find(idx, coins, sum):

        # BASE CASE
        if(sum == 0):
            return 0
        
        if(sum < 0 or idx == len(coins)):
            return float('inf')
        

        take = float('inf')
        
        if(coins[idx] > 0):
            take = reCur_find(idx, coins, sum - coins[idx])

            if(take != float('inf')):
                take += 1

        nottake = reCur_find(idx + 1, coins, sum)
        
        return min(take, nottake)
    
    result = reCur_find(0, coins, amount)
    return -1 if(result ==float('inf')) else result

# TABULATION 
# time : O(N* AMOUNT)
# space : O(N * AMOUNT)
"""
coins = [1,5,10], amount = 12

dp [] 

ans = 3
"""
def coinChange(self, coins, amount: int) -> int:
    
    dp = [[0] * (amount + 1) for _ in range(len(coins))] # 2D table

    for i in range(len(coins)-1, -1, -1):

        for j in range(1, amount + 1):

            dp[i][j] = float('inf')
            take = float('inf')
            nottake = float('inf')
            
            # amount - curr coin >= 0
            if(j - coins[i] >= 0 and coins[i] > 0):
                take = dp[i][j - coins[i]]
                
                if(take != float('inf')):
                    take += 1

            if(i + 1 < len(coins)):
                nottake = dp[i + 1][j]

            dp[i][j] = min(take, nottake)
    
    return -1 if dp[0][sum] != float('inf') else dp[0][sum]

# OPTIMIZED DP 
# time : O(N*AMOUNT)
# space : O(AMOUNT)
def coinChange(self, coins, amount: int) -> int:
        
    dp = [float('inf')] * (amount + 1) # 1D 

    # BASE
    dp[0] = 0

    for i in range(len(coins)-1, -1, -1):
        for j in range(1, amount + 1):

            take = float('inf')
            nottake = float('inf')

            if(j - coins[i] >= 0 and coins[i] > 0):
                take = dp[j - coins[i]] 

                if(take != float('inf')):
                    take += 1

            if(i + 1 < len(coins)):
                nottake = dp[j]
                
            dp[j] = min(take, nottake)

    return -1 if(dp[amount] == float('inf')) else dp[amount]

