import sys
input = sys.stdin.readline
from itertools import combinations

# 카드의 개수 n과 m
n, m = map(int, input().split())

# 카드 리스트
cards = list(map(int, input().split()))

# 합이 m을 넘지 않으면서 가장 가까운 3장의 합 출력
maxvalue = 0

for value in combinations(cards, 3):
    if sum(value) <= m:
        if sum(value) > maxvalue:
            maxvalue = sum(value)

print(maxvalue)