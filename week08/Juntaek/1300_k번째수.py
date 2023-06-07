# #B를 오름차순 b[k] 구해보자.
N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N)

    if temp >= K:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)