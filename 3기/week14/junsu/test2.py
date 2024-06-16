# [가르침](https://www.acmicpc.net/problem/1062)

# 1차 시도
import sys

n, k = map(int, sys.stdin.readline().split())
words = []
for _ in range(n):
    tmp = sys.stdin.readline().strip()
    words.append(tmp)
answer = 0
arr = []
for word in words:
    word = word[4:-4]
    cnt = 0
    for w in word:
        if w in ['a', 'n', 't', 'i', 'c']:
            continue
        cnt += 1
        arr.append(cnt)


print(answer)
