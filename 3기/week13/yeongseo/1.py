class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = []
        
        idx = 0
        
        strs.sort(key = lambda x : len(x))
        
        while idx < len(strs[0]):
            first = strs[0][idx]
            
            same = True
            for s in strs:
                if s[idx] != first:
                    same = False
                    break
            
            if not same:
                break
            
            ans.append(first)
            
            idx += 1
        
        return ''.join(ans)
        
Solution().longestCommonPrefix(["flower","flow","flight"])