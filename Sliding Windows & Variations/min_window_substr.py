from collections import Counter
def minWindow(self, s: str, t: str) -> str:
    
    _window = Counter()
    _required = Counter(t)
    _window_count = 0

    left= 0 
    minlen = 0

    for right in range(len(s)):
        _window[s[right]] = _window.get(s[right],0) + 1

        if(s[right] in _required and _required[s[right]]==_window[s[right]]):
            _window_count += 1

        while(len(_required) == _window_count):
            # valid window 
            # start shrinking

            if(right - left + 1 < minlen):
                minlen = right-left+1
            
            _window[s[left]] -= 1
            if(s[left] in _required and _window[s[left]] < _required[s[left]]):
                _window_count -= 1

            left += 1

    return minlen

