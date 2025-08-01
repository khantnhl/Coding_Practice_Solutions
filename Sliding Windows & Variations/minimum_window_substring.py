"""
uses two hashmaps, haves and needs to keep track
"""
def minWindow(self, s: str, t: str) -> str:
    
    from collections import Counter
    t_map = Counter(t)

    needs = len(t_map)
    have = 0

    left = 0
    curWindow = {}
    resLength = float('inf')
    result = [-1,-1]
    for right in range(len(s)):
        ch = s[right]
        curWindow[ch] = curWindow.get(ch, 0) + 1

        if(ch in t_map and curWindow[ch] == t_map[ch]):
            have += 1
        
        while(have == needs):
            if(right-left+1 < resLength):
                resLength = right - left + 1
                result = [left, right]
            
            curWindow[s[left]] -= 1
            if(s[left] in t_map and curWindow[s[left]] < t_map[s[left]]):
                have -= 1
            
            left += 1
    

    if(resLength == float('inf')):
        return ""
    else:
        return s[result[0] : result[1] + 1]
