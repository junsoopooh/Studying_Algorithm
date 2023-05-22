import sys
input = sys.stdin.readline

# 배열의 크기 N
n = int(input())
k = int(input())

start = 0
end = k

result = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in range(1, n+1):
        count += min(mid//i, n)

    if count >= k:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)