"""
코코넛 그 두 번째 이야기
문제: https://www.acmicpc.net/problem/6417
"""
import sys

input = sys.stdin.readline

def check(num):
    ans = 0
    for i in range(1, num+1):
        tmp = num
        cnt = 0
        while 1:
            tmp -= 1 # 원숭이한테 1개 주고
            if tmp % i == 0:
                tmp = tmp - tmp // i # 자기 몫 챙기고
                cnt += 1
                if not tmp:
                    break
            else:
                break
        if i == cnt:
            ans = max(ans, i)
    return ans

while 1:
    n = int(input())

    if n == -1:
        sys.exit(0)

    ans = check(n)

    if ans == 1:
        print(str(n) + " coconuts, " + "no solution")
    else:
        print(str(n) + " coconuts, " + str(ans) + " people and " + str(1) + " monkey")