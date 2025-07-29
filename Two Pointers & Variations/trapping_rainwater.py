from typing import List

"""
    time : O(n)
    space: O(n) can be optimized -> O(1) Check below

            [0,2,0,3,1,0,1,3,2,1]

    finding max values at each index to the left and right
    maxleft: [0,0,2,2,3,3,3,3,3,3]
    maxright:[3,3,3,3,3,3,3,2,1,0] #start from end

    minimum: [0,0,2,2,3,3,3,2,1,0]
    formula : minimum(left, right) - height[index]
    -2 2 -1 2 3 2 -1 -1 -1
    but if you ignore the negatives, you get the answerL 9
"""

def trap(height: List[int]) -> int:
    if(not height):
        return 0
    
    maxleft = [0] * len(height)
    maxright= [0] * len(height)

    # because at the beginning of maxleft and 
    # end of maxright there were no maximum value to take 
    maxleft[0] = height[0]
    maxright[-1] = height[-1]
    result = 0

    for i in range(1, len(height)):
        maxleft[i] = max(height[i], maxleft[i-1])

    for i in range(len(height)-2, -1, -1):
        maxright[i] = max(height[i], maxright[i+1])

    for i in range(len(height)):
        curSum = min(maxleft[i], maxright[i]) - height[i]

        if(curSum < 0):
            continue
        result += curSum

    return result 
            
"""
Optimal
time: O(n)
space: O(1)

    [0,2,0,3,1,0,1,3,2,1]
     l                 r 
     lm                rm  
"""
def trap(height: List[int]) -> int:
    if(not height):
        return 0

    left = 0
    right = len(height)-1

    leftMax = height[left]
    rightMax = height[right]
    result = 0

    while(left < right):
        if(leftMax < rightMax):
            left += 1
            leftMax = max(leftMax, height[left])

            result += leftMax - height[left]
        else:
            right -= 1
            rightMax = max(rightMax, height[right])

            result += rightMax - height[right]    

    return result  