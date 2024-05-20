# [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        for i in range(1, len(strs)):
            for j in range(1, len(word)+1):
                if word[:j] != strs[i][:j]:
                    word = word[:j-1]
                    break
        return word
