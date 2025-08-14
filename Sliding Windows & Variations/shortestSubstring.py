# "abracadabra", "abc" (required)
"""
{
a:1
b:1
c:1
}
requiredCount = len(required) = 3
"""

def shortestsubstring(s : str, t : str) -> int:
    from collections import Counter
    required = Counter(t)

    minLen = float('inf')
    left = 0
    curWindow = {}
    curCount = 0

    for right in range(len(s)):
        
        if(s[right] in required):
            curWindow[s[right]] = curWindow.get(s[right],0) + 1

            # same counts
            if(required[s[right]]==curWindow[s[right]]):
                curCount += 1
        
        while(curCount == len(required)):
            minlen = min(minlen, right-left+1)

            # outgoing
            if(s[left] in required):
                curWindow[s[left]] -= 1

                if(curWindow[s[left]] < required[s[left]]):
                    curCount -= 1
            left += 1

    return minlen
        
        
