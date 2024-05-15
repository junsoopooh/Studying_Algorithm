# [two-sum](https://leetcode.com/problems/two-sum/description/)
# 1차시도 : [-3,4,3,90],0 일때 틀림
class Solution:
    def twoSum(self, nums, target: int):
        board = dict()
        idx_arr = dict()
        answer = []
        for i in range(len(nums)):
            if nums[i] not in board:
                board[nums[i]] = 1
            else:
                board[nums[i]] += 1

        for i in range(len(nums)):
            if nums[i] not in idx_arr:
                idx_arr[nums[i]] = [i]
            else:
                idx_arr[nums[i]].append(i)
        for i in range(-target,target+1,1):
            if i in board and target-i in board:
                if i != target-i:
                    answer = [idx_arr[i][0],idx_arr[target-i][0]]
                    break
                else:
                    if board[i] >= 2:
                        answer = [idx_arr[i][0], idx_arr[i][1]]
                        break
        return answer

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i,j]

