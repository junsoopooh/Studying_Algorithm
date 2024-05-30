"""
Container With Most Water
https://leetcode.com/problems/container-with-most-water/description/
"""


class Solution:
    def maxArea(self, height):
        answer = 0

        left, right = 0, len(height) - 1

        while left <= right:
            width = right - left
            tmp = min(height[right], height[left]) * width
            answer = max(answer, tmp)

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return answer
