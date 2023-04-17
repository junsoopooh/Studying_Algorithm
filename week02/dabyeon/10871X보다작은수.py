import sys
input = sys.stdin.readline

N, X = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

result = []
for num in nums:
    if num < X:
        result.append(num)

print(*result)