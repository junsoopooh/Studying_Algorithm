import sys
input = sys.stdin.readline
from itertools import permutations

# n장의 카드
n = int(input())

# 그 중 k장의 카드 선택
k = int(input())

# n장의 카드들
cards = [input().strip() for _ in range(n)]

result = set()

for card in permutations(cards, k):
    result.add("".join(card))

print(len(result))