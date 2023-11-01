import sys
input = sys.stdin.readline
from itertools import combinations

n, s = map(int, input().split())
values = list(map(int, input().split()))

# 부분 수열은 수열에서 이어져 있지 않아도 되나?

count = 0
for i in range(1, n+1):
    for j in combinations(values, i):
        if sum(j) == s:
            count += 1

print(count)