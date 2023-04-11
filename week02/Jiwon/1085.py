import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

# left = x
# right = w-x
# up = h-y
# down = y

print(min(x, y, w-x, h-y))