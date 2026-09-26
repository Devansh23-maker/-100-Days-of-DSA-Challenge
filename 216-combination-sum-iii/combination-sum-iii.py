class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []

        def backtrack(i, current_sum, path):

            if len(path) == k:
                if current_sum == n:
                    res.append(path)
                return

            if i > 9 or current_sum > n:
                return
        
            backtrack(i + 1, current_sum + i, path + [i])
            backtrack(i + 1, current_sum, path)

        backtrack(1, 0, [])
        
        return res