import sys
input = sys.stdin.readline

values = [int(input()) for _ in range(9)]

print(max(values))
print(values.index(max(values)) + 1)