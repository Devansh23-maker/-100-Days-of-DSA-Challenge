class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(i, current_sum, path):
            if current_sum == target:
                res.append(path)
                return
            if i >= len(candidates) or current_sum > target:
                return
            
            backtrack(i, current_sum + candidates[i], path + [candidates[i]])

            backtrack(i + 1, current_sum, path)
        
        backtrack(0, 0, [])
        return res