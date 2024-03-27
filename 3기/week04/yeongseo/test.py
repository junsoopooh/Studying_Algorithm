class Solution(object):
    def characterReplacement(self, s, k):
        lo = 0
        hi = 0
        letters = {}
        ans = 1
        
        while hi < len(s):
            if s[hi] in letters.keys():
                letters[s[hi]] += 1
            else:
                letters[s[hi]] = 1
            
            # 현 상황
            all_letters = hi - lo + 1 
            max_letter = 0
            max_letter_cnt = 0
            for key in letters.keys():
                if letters[key] > max_letter_cnt:
                    max_letter = key
                    max_letter_cnt = letters[key]
            
            if all_letters - max_letter_cnt > k:
                if letters[s[lo]] == 1:
                    del letters[s[lo]]
                else:
                    letters[s[lo]] -= 1
                lo += 1
            else:
                ans = max(ans, all_letters)
                hi += 1
        
        return ans
                    

print(Solution().characterReplacement("AABABBA", 1))