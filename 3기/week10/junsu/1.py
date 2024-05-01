# [Score of a String](https://leetcode.com/problems/score-of-a-string/description/)
class Solution:
    def scoreOfString(self, s: str) -> int:
        answer = 0
        for i in range(len(s)-1):
            answer += abs(ord(s[i]) - ord(s[i+1]))
        return answer