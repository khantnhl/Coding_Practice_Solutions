from typing import List
def permutation(nums : List[int]):

    result = []

    # base case 
    if(len(nums)==1):
        return [nums.copy()]
    
    for i in range(len(nums)):
        hold = nums.pop(0)

        perms = permutation(nums)

        for perm in perms:
            perm.append(hold)
        
        result.extend(perms)
        nums.append(hold) # reappend cuz we popped

    return result

# time : n!
