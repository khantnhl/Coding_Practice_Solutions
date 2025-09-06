"""
time : O(log(min(n, m)))
space: O(1)
"""

def findMedianSortedArrays(self, nums1, nums2) -> float:

    if(len(nums2) < len(nums1)):
        nums1, nums2 = nums2, nums1

    left = 0
    right = len(nums1)
    total_len = len(nums1) + len(nums2)
    median = 0

    while(True):
    
        i = (left + right) // 2
        j = total_len//2 - i - 2

        Aleft = nums1[i] if(i >= 0) else float('-inf') 
        Aright = nums1[i + 1] if(i < len(nums1)-1) else float('inf')

        Bleft = nums2[j] if(j >= 0) else float('-inf') 
        Bright = nums2[j + 1] if(j < len(nums2)-1) else float('inf')

        # valid condition 
        # boundaries should never cross
        if(Aleft <= Bright and Bleft <= Aright):
            if(total_len % 2 == 0): # even
                return (max(Aleft, Bleft)+ min(Aright, Bright)) / 2
            else: # odd
                return min(Aright, Bright)

        elif(Aleft > Bright):
            right = i - 1
        else:
            left = i + 1