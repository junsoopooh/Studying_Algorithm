import sys

x,y,w,h = map(int,sys.stdin.readline().split())

ans = min(x,w-x,y,h-y)
print(ans)