import sys
from heapq import heappop, heappush
n = int(sys.stdin.readline())
cards = []
for _ in range(n):
    card = int(sys.stdin.readline())
    heappush(cards,card)

cnt = 0
ans = 0

if n == 1:
    ans = 0

elif n == 2:
    tmp1 = heappop(cards)
    tmp2 = heappop(cards)
    ans = tmp1 + tmp2

else:
    while len(cards) > 1:
        tmp1 = heappop(cards)
        tmp2 = heappop(cards)
        tmp = tmp1 + tmp2
        ans += tmp
        heappush(cards,tmp)
ans += heappop(cards)
print(ans)