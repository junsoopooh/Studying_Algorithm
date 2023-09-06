import sys

n = int(sys.stdin.readline())
arr = set(list(map(int, sys.stdin.readline().split())))
arr = list(arr)
arr.sort()
print(*arr)
