"""
    use hashmap to store prefix values along with counts
    initialized {0 : 1} for first current summation
    curSum - k as key 
"""

def subarraySum(self, nums: List[int], k: int) -> int:
    
    curSum = 0
    result = 0
    _prefix_map = {0 : 1}

    for num in nums:
        curSum += num

        result += _prefix_map.get(curSum - k, 0)
        _prefix_map[curSum] = _prefix_map.get(curSum,0) + 1

    return result