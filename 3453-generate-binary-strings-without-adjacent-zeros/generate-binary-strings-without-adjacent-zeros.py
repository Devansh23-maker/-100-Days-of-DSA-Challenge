class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def solve(i, s):
            if i == n:
                ans.append(s)
                return
            
            if s and s[-1] == '0':
                solve(i + 1,s + '1')
            
            else:
                solve(i+1, s + '0')
                solve(i+1, s + '1')
                
        solve(0, "")
        return ans