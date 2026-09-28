class Solution:
    def partition(self, s: str) -> list[list[str]]:
        path =[]
        res = []
        start = 0
        def backtrack(start):
            if start == len(s):
                res.append(path[:])

            for i in range(start, len(s)):
                part = s[start:i + 1]

                if part == part[::-1]:
                    path.append(part)
                    backtrack(i+1)
                    path.pop()
        
        backtrack(0)
        return res