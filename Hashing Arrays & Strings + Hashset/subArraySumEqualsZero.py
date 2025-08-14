# use hashmap and prefix sum
# if same sum appears again in HASHMAP 
# that means there must have been negative numbers that sum to ZERO

def ZeroSumSubArray(nums : list[int]) -> int : 

    _count = 0 
    prefix = [0] * (len(nums)+1)

    # 0 : 1 to count in zero itself
    _freq = { 0 : 1 }

    for i in range(len(nums)):
        prefix[i+1] = prefix[i] + nums[i]

        if(prefix[i+1] in _freq):
            _count += _freq[prefix[i+1]]
        
        # add to HashMap
        _freq[prefix[i+1]] = _freq.get(prefix[i+1],0) + 1

    return _count