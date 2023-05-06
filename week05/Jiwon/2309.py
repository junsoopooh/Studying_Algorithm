import sys
input = sys.stdin.readline
from itertools import combinations

shorts = [int(input()) for _ in range(9)]
results = []

for value in combinations(shorts, 7):
    if sum(value) == 100:
        results = list(value)
        break

results.sort()

for result in results:
    print(result)