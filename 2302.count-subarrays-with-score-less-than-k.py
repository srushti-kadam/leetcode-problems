class Solution(object):
    def countSubarrays(self, nums, k):
        n = len(nums)
        left = 0
        total = 0
        window_sum = 0
        count = 0

        for right in range(n):
            window_sum += nums[right]
        
            while window_sum * (right - left + 1) >= k:
                window_sum -= nums[left]
                left += 1
        
            count += (right - left + 1)

        return count
        
