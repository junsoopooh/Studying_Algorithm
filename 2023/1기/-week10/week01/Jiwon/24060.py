import sys
input = sys.stdin.readline

def merge_sort(arr, p, r):
    if p < r:
        # q는 p, r의 중간 지점
        q = (p+r) // 2

        # 전반부 정렬, 후반부 정렬, 병합
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    i = p
    j = q+1
    t = 0

    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            t += 1
            i += 1
        else:
            tmp[t] = arr[j]
            t += 1
            j += 1

    # 왼쪽 배열 부분이 남은 경우
    while i <= q:
        tmp[t] = arr[i]
        t += 1
        i += 1
    
    # 오른쪽 배열 부분이 남은 경우
    while j <= r:
        tmp[t] = arr[j]
        i += 1
        j += 1

    i = p
    t = 0

    while i <= r:
        arr[i] = tmp[t]
        result.append(arr[i])
        i += 1
        t += 1

# 배열의 크기, 저장 횟수
n, k = map(int, input().split())

# 배열 원소
values = list(map(int, input().split()))

tmp = [0] * n

# 저장되는 수를 차례대로 저장
result = []

merge_sort(values, 0, len(values)-1)

if len(result) < k:
    print(-1)
else:
    print(result[k-1])