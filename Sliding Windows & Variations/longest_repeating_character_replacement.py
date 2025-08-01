"""
time : O(n)
space: O(n)
"""
def characterReplacement(self, s: str, k: int) -> int:
    
    _freq = {}
    max_freq = 0
    maxlen = 0
    left=0
    for right in range(len(s)):

        _freq[s[right]] = _freq.get(s[right], 0) + 1
        max_freq = max(max_freq, _freq[s[right]])

        while((right-left+1) - max_freq > k):
            if(_freq[s[left]] > 1):
                _freq[s[left]] -= 1
            else:
                del _freq[s[left]]

            left += 1

        maxlen = max(maxlen, right-left+1)

    return maxlen