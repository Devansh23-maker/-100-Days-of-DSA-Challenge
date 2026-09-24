class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        left = 0 
        right = len(nums) - 1
        ans = 0
        MOD = 10**9 + 7
    
        while left <= right:
            if nums[left] + nums[right] <=  target:
                ans += 2 ** (right - left)
                left += 1
            else:
                right -= 1
    
        return ans % MOD