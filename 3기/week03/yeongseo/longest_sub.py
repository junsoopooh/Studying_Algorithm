class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        max_len = 0
        chars = set()
        lo = 0

        for hi in range(len(s)):
            if s[hi] not in chars:
                chars.add(s[hi])
                max_len = max(max_len, hi - lo + 1)
            else:
                while s[hi] in chars:
                    chars.remove(s[lo])
                    lo += 1
                chars.add(s[hi])

        return max_len

print(Solution().lengthOfLongestSubstring("dvdf"))