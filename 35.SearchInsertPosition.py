class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return(nums.index(target))
        else:
            i = 0
            for n in nums:
                if n > target:
                    return i
                else:
                    i += 1
            return i

#binary search approach

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
