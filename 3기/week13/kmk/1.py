"""
Longest Common Prefix
문제: https://leetcode.com/problems/longest-common-prefix/description/
"""


class Solution:
    def longestCommonPrefix(self, strs):

        if len(strs) == 1:
            return strs[0]

        ans = ""
        strs.sort()

        min_val, max_val = strs[0], strs[-1]

        for i in range(len(min_val)):
            if (min_val[i] == max_val[i]):
                ans += min_val[i]
            else:
                break

        return ans