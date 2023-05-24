import sys
input = sys.stdin.readline

# 집의 개수, 공유기의 개수
n, m = map(int, input().split())

# 집의 좌표
houses = [int(input()) for _ in range(n)]
houses.sort()

# 이번에는 두 공유기 사이 거리가 minvalue, maxvalue 겠네
minvalue = 1
maxvalue = houses[-1] - houses[0]

count = 0
result = 0

while minvalue <= maxvalue:
    mid = (minvalue + maxvalue) // 2

    # m 개의 공유기를 다 설치해야 함
    # 가장 인접한 공유기의 "최대 거리"를 구하는 것

    # 항상 첫번째 집에 설치하면 되나?
    now = houses[0]
    count = 1

    for i in range(1, n):
        # 만약 설치할 수 있다면,
        if houses[i] >= now + mid:
            now = houses[i]
            count += 1

    # 설치한 공유기 개수가 모자라면,
    # 거리를 좁혀야겠지
    if count < m:
        maxvalue = mid - 1
    else:
        result = mid
        minvalue = mid + 1

print(result)