"""
주식 가격
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42584
"""

def solution(prices):
    answer, n = [], len(prices)

    for i in range(n - 1):
        t = n - i - 1
        for j in range(i + 1, n):
            if prices[j] < prices[i]:
                t = j - i
                break
        answer.append(t)
    return answer + [0]