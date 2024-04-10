"""
소수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/42839
"""

"""
1. 에라토스테네스의 체
2. 백트래킹
"""

answer = 0

def solution(numbers):
    prime = [1] * 10000000
    prime[0] = prime[1] = 0
    for i in range(2, int(10000000 ** 0.5) + 1):
        if prime[i]:
            for j in range(i + i, 1000000, i):
                prime[j] = 0
    numbers = list(numbers)

    n = len(numbers)
    check = [0] * n
    res = []
    a = set()

    def dfs():
        global answer

        if res:
            if res[0] != "0":
                if prime[int("".join(res))] == 1:
                    a.add(int("".join(res)))

        for i in range(len(numbers)):
            if not check[i]:
                check[i] = 1
                res.append(numbers[i])
                dfs()
                res.pop()
                check[i] = 0

    dfs()
    return len(a)