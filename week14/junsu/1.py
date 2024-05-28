# [Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)

# 1차시도: 시간초과(50/62)
class Solution:
    def check(self,a,b,height):
        val = min(height[a], height[b])
        return abs(b-a)*val

    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        for a in range(n-1):
            for b in range(a+1,n):
               ans = max(ans, self.check(a,b,height))
        return ans 
    
# 2차시도: 메모리초과(49/62)
from itertools import combinations

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        tmp = [i for i in range(len(height))]
        arr = list(combinations(tmp,2))
        for case in arr:
            w = abs(case[0]-case[1])
            h = min(height[case[0]], height[case[1]])
            ans = max(ans, w*h)
        return ans
    
# 3차시도: 성공(62/62)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height)-1
        while left < right:
            mid = (left+right)//2
            w = right-left
            h = min(height[left],height[right])
            ans = max(ans, w*h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans