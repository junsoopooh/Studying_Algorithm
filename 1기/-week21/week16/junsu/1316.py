import sys

n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    arr = set()
    k = len(word)
    tmp = word[0]
    for i in range(1,k):
        if tmp != word[i]:
            arr.add(tmp)
            tmp = word[i]
        if tmp in arr:
            break
    else:
        cnt += 1
print(cnt)