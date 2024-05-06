# [소수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12977)
from itertools import combinations

def solution(nums):
    answer = 0
    board = [False for _ in range(3001)]
    board[2] = board[3] = True

    for num in range(4,3001):
        for i in range(2,num):
            if not num%i:
                break
        else:
            board[num] = True
            
    nCr = list(combinations(nums,3))
    for i in nCr:
        if board[sum(i)]:
            answer += 1

    return answer