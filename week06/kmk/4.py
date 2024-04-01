"""
가장 큰 수
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42746
"""
"""
1. 주어진 값 더해서 0이면 그냥 리턴
2. 주어진 배열 전부 문자열로 변환
3. 어차피 정답은 최대 100,000 * 1000 = 100,000,000로 9자리이다. 각 자리수 9자리에 근접하게 만들어보면 된다.
4. 정렬 후 리턴
"""

def solution(numbers):
    if sum(numbers) == 0:
        return "0"

    nums = list(map(str, numbers))

    for i in range(len(nums)):
        nums[i] = [nums[i], nums[i] * (9 // len(nums[i]))]

    nums.sort(key=lambda x: x[1], reverse=True)

    return "".join(s[0] for s in nums)