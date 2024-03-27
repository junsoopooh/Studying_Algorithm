"""
랜선 자르기
문제: https://www.acmicpc.net/problem/1654
"""
import sys

input = sys.stdin.readline

k, n = map(int, input().split())

nums = [int(input()) for _ in range(k)]

start, end = 1, max(nums)

ans = 0

while start <= end:
    mid = (start + end) // 2

    cnt = sum(num // mid for num in nums)

    if cnt >= n:
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1

print(ans)