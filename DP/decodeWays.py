# Tabulation method, Optimal solution below
"""
    idea is to use: 
        - dp table array 
        - initialized last cell to 1 becuz empty cell is 1
"""
def numDecodings(self, s: str) -> int:
    n = len(s)

    dp = [0] * (n + 1)
    dp[n] = 1 # empty str -> 1

    for i in range(n - 1, -1, -1):
        
        if(s[i] != '0'):
            dp[i] = dp[i + 1]

        if(i < n - 1 and 
          (s[i]=='1' and s[i + 1] <='9') or 
          (s[i]=='2' and s[i + 1] <= '6')):
            dp[i] = dp[i + 2]

    return dp[0]


"""
s = "12" -> AB (1 or 2) or L (12)


    use two pointers prev1, prev2 
    iterate from 1 to len + 1
    check single digit [i - 1] 
    reconstruct to validate two-digit number 
    [i-2] * 10 + [i - 1]
"""
# OPTIMIZED SPACE
def numDecodings(self, s: str) -> int:
    n = len(s)
    if(not s):
        return 0
    
    if(s[0] == '0'):
        return 0
    
    prev1 = 1 # last pointer
    prev2 = 0

    for i in range(1, n + 1):
         
        current = 0 # track

        # do nothing for zero case
        # check non-zero
        if(s[i - 1] != '0'):
            current += prev1 

        if(i > 1): # we can construct two digit number
            twoDigit = int(s[i-2]) * 10 + int(s[i-1])

            if(10 <= twoDigit <= 26):
                current += prev2

        prev2 = prev1
        prev1 = current
    
    return prev1
