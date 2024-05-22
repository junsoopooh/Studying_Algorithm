"""
모의고사
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42840
"""
"""
정답 배열 길이에 맞게 수포자 1,2,3 길이 늘려주거나 줄여주면 됨
"""

def solution(answers):
    n = len(answers)

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    one = one[:n] if len(one) >= n else one * (n - len(one))
    two = two[:n] if len(two) >= n else two * (n - len(two))
    three = three[:n] if len(three) >= n else three * (n - len(three))

    ans = [0] * 3

    for i in range(n):
        if answers[i] == one[i]:
            ans[0] += 1
        if answers[i] == two[i]:
            ans[1] += 1
        if answers[i] == three[i]:
            ans[2] += 1

    max_val = max(ans)

    return [i + 1 for i in range(3) if ans[i] == max_val]