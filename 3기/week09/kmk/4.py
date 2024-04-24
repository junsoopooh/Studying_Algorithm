"""
별 찍기 - 10
문제: https://www.acmicpc.net/problem/2447
"""
n = int(input())

def recur(num):

    if num == 1:
        return ["*"]

    star = recur(num // 3)

    ans = []

    for f in star:
        ans.append(f*3)
    for s in star:
        ans.append(s + " "*(num//3) + s)
    for t in star:
        ans.append(t*3)

    return ans

print("\n".join(recur(n)))
