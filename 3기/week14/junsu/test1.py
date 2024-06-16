# [Unique Paths](https://leetcode.com/problems/unique-paths/description/)

# A가 a개, B가 b개 있을 때 정렬하는 경우의 수는 (a+b)!/(a!b!)이다.
# down m-1개, right n-1개를 정렬하는 경우의 수는 (m+n-2)!/(m-1)!(n-1)!이다.
class Solution:
    def factorial(k: int) -> int:
        cnt = 1
        for i in range(1,k+1):
            cnt *= i
        return cnt
    def uniquePaths(self, m: int, n: int) -> int:
        a = Solution.factorial(k=(m+n-2))
        b = Solution.factorial(k=(m-1))
        c = Solution.factorial(k=(n-1))
        d = b*c
        return a//d