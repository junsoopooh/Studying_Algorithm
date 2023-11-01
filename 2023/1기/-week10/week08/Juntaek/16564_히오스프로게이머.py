## 다시풀어보기 ##
N, K = map(int, input().split())
level = [int(input()) for _ in range(N)]
# print(level)

start, end = 1, max(level)+K
while start <= end:
    mid = (start+end)//2
    result = 0
    for i in level:
        if mid > i:
            result += (mid-i)
    if result <= K:
        answer = mid
        start = mid+1
    else:
        end = mid-1
print(answer)