class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)
        memo = {}

        def backtrack(index, current_sum):
            if current_sum == target:
                return True
            if index == n or current_sum > target:
                return False
            
            key = (index, current_sum)
            if key in memo:              # yeh state pehle solve ho chuki hai?
                return memo[key]          # seedha wahi answer de do, dobara mat calculate karo
            
            memo[key] = backtrack(index + 1, current_sum + nums[index]) or backtrack(index + 1, current_sum)
            return memo[key]

        return backtrack(0, 0)