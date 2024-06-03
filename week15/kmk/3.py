"""
구명보트
https://school.programmers.co.kr/learn/courses/30/lessons/42885
"""

def solution(people, limit):
    ans = 0

    people.sort()

    left, right = 0, len(people) - 1

    while left <= right:
        if people[left] + people[right] <= limit:
            ans += 1
            left += 1
            right -= 1
        else:
            ans += 1
            right -= 1
    return ans