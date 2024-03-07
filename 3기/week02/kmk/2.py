"""
둘만의 암호
https://school.programmers.co.kr/learn/courses/30/lessons/155652
"""
def solution(s, skip, index):
    skip = [ord(c) for c in skip]

    nums = [i for i in range(97, 123) if i not in skip] * 4

    ans = ""

    for c in s:
        ans += chr(nums[nums.index(ord(c)) + index])

    return ans
