# import itertools
# import sys
# input = sys.stdin.readline
# n = int(input())
# k = int(input())
# cards = []
# for _ in range(n):
#     cards.append(int(input()))
# nPk = itertools.permutations(cards, k)
# nPk = list(set(nPk))
# print(nPk)
# print(len(nPk))

### 순열 라이브러리 이용 ###
# import itertools
# import sys
# input = sys.stdin.readline
# n, k = int(input()), int(input())
# cards = [input().rstrip() for _ in range(n)]
# permutations = itertools.permutations(cards, k)
# res = set()
# print(list(permutations))
# for per in permutations:
#     res.add(''.join(per))
# print(res)

### 재귀 함수로 순열 구현 ###
import sys
input = sys.stdin.readline
n, k = int(input()), int(input())
cards_array = [input().rstrip() for _ in range(n)]
array = set()

def permutation(cnt, perm, visit):
    global cards_array
    if cnt==k:
        array.add(''.join(perm))
        return
    for idx in range(n):
        if not visit[idx]:
          visit[idx] = 1
          permutation(cnt+1, perm+[cards_array[idx]], visit)
          visit[idx] = 0

permutation(0, [], [0]*n)
print(len(array))