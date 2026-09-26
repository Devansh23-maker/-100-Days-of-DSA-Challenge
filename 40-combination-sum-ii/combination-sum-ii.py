class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(i, current_sum, path):

            if current_sum == target:
                res.append(path)
                return

            if i >= len(candidates) or current_sum > target:
                return 
            
            backtrack(i+1, current_sum + candidates[i], path + [candidates[i]]
            )

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            backtrack(i+1, current_sum, path)

        backtrack(0, 0, [])
        return res
        