class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        even_count = (n + 1) //2
        odd_count = n // 2

        even = pow(5, even_count, MOD)
        odd = pow(4, odd_count, MOD)

        return (even * odd) % MOD
