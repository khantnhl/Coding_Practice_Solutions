"""
Expand from center
"""

def longestPalindrome(self, s: str) -> str:
    result = 0
    res_str = ""
    
    for i in range(len(s)):
        left, right = i, i 
        
        while(left >= 0 and right < len(s) and s[left] == s[right]):

            if(right - left + 1 > result):
                result = right - left + 1
                res_str = s[left : right +1]

            left -= 1
            right += 1

    for i in range(len(s)):
        left = i
        right = i + 1
        while(left >= 0 and right < len(s) and s[left]==s[right]):
            
            if(right-left+1 > result):
                result = right - left + 1
                res_str = s[left : right + 1]

            left -= 1
            right += 1

    return res_str