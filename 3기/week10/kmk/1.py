"""
Score of a String
문제: https://leetcode.com/problems/score-of-a-string/
"""

class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1):
            ans += abs(ord(s[i]) - ord(s[i+1]))
        return ans