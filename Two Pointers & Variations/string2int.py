"""
"   -042"
        i   
"""

def myAtoi(self, s: str) -> int:
    if(not s):
        return 0

    idx = 0
    while(idx < len(s) and s[idx]==' '):
        idx += 1
    
    if(idx == len(s)): return 0
    
    sign = 1
    if(s[idx] in ['-', '+']):
        sign = -1 if(s[idx]=='-') else sign
        idx += 1

    
    result = 0
    MAXINT = (2**31-1)//10 # ROUND UP
    
    while(idx < len(s)):

        if(not s[idx].isdigit()):
            break
        
        digit = int(s[idx])

        # overflow cases
        if(result > MAXINT or (result == MAXINT and digit > 7)):
            if(sign==1):
                return 2 ** 31 - 1
            else:
                return -2 ** 31

        result = result * 10 + digit
        idx += 1

    return sign * result

