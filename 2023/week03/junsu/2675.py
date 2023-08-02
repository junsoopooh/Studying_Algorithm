import sys

t = int(sys.stdin.readline())

for _ in range(t):
    arr = list(sys.stdin.readline().rstrip().split())
    r = int(arr[0])
    word = list(arr[1])
    for i in range(len(word)):
        word[i] = r*word[i]
    print(*word,sep='')
