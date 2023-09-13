import sys
from itertools import permutations

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

cards = []
for _ in range(n):
    card = sys.stdin.readline().rstrip()
    cards.append(card)

arr = set()
for x in permutations(cards, k):
    arr.add(''.join(x))

print(len(arr))