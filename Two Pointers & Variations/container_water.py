"""
time : O(n)
space: O(1)
"""
def maxArea(heights: List[int]) -> int:
        
        """
        [1,7,2,5,4,7,3,6]
         l             r
        """

        left, right = 0, len(heights)-1
        maxRes = float('-inf')

        while(left < right):
            
            maxRes = max(maxRes, min(heights[left], heights[right]) * (right-left))

            if(heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
  
        return maxRes