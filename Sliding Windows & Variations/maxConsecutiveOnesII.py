
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    left = 0 
    maxlen = float('-inf')
    _freq = {}
    maxOnes = 0

    for right in range(len(nums)):
        _freq[nums[right]] = _freq.get(nums[right],0) + 1
        
        if(nums[right]==1):
            maxOnes += nums[right]

        while((right-left+1) - maxOnes > 1): # at most One Flip
            if(nums[left]==1): 
                maxOnes-=1
            _freq[nums[left]] -= 1
            left += 1

        maxlen = max(maxlen, right-left+1)


    return maxlen if(maxlen!=float('-inf')) else -1