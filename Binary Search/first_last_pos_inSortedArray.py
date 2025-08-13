def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def find(nums, target, searchleft):

            left, right = 0, len(nums)-1
            ans = -1

            while(left <= right):
                mid = (left + right)//2
                
                if(nums[mid] < target):
                    left = mid + 1
                elif(nums[mid] > target):
                    right = mid - 1
                else:
                    ans = mid

                    if(searchleft):
                        right = mid -1
                    else:
                        left = mid + 1
            return ans
                
        first = find(nums, target, True)
        last = find(nums, target, False)
        return [first,last]