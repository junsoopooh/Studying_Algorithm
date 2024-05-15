"""
Two Sum
문제: https://leetcode.com/problems/two-sum/description/
"""

class Solution:
    def twoSum(self, nums, target):
        nums = sorted(enumerate(nums), key=lambda x: x[1])
        start, end = 0, len(nums) - 1
        ans = [0, 0]
        while start < end:
            tmp = nums[start][1] + nums[end][1]
            if tmp < target:
                start += 1
            elif tmp > target:
                end -= 1
            else:
                ans[0], ans[1] = nums[start][0], nums[end][0]
                break

        return ans
