"""
포켓몬
https://school.programmers.co.kr/learn/courses/30/lessons/1845
"""

def solution(nums):
    target = len(nums) // 2
    set_nums = set(nums)

    if len(set_nums) > target:
        return target
    else:
        return len(set_nums)