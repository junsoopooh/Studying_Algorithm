class Solution(object):
    def twoSum(self, nums, target):
        new_nums = []
        for i in range(len(nums)):
            new_nums.append((i, nums[i]))
        
        new_nums.sort(key = lambda x : x[1])
        
        lo = 0
        hi = len(new_nums) - 1
        
        while True:
            summ = new_nums[lo][1] + new_nums[hi][1]
            if summ == target:
                return [new_nums[lo][0], new_nums[hi][0]]
            
            elif summ < target:
                lo += 1
            
            else: 
                hi -= 1 
        