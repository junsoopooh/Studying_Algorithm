class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        return (pow(20 , (n//2),mod) * pow(5 , (n%2),mod)) % mod
        

