def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
    
    """keep dividing and use Hashset to store prefixes"""
    
    prefix_set = set()
    maxlen = 0

    for num in arr1:
        while(num):
            prefix_set.add(num)
            num = num // 10

    for num in arr2:
        while(num):
            if(num in prefix_set):
                maxlen = max(maxlen, len(str(num)))
                break
            num = num // 10

    return maxlen