"""
Build Array From Permutation
문제: https://leetcode.com/problems/build-array-from-permutation/description/
"""

class Solution:
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))]