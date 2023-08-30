import sys
from heapq import heappop, heappush

input = sys.stdin.readline

# 사람의 수
n = int(input())

# 집 사무실
houses = []

for _ in range(n):
    house, office = map(int, input().split())

    # 큰 수가 앞에 올 수 있으니, [작은 수, 큰 수]
    if house < office:
        houses.append([house, office])
    else:
        houses.append([office, house])

# 사무실 (뒤의 값) 위치의 오름차순
houses.sort(key=lambda x: x[1])

# 철로의 길이
railway = int(input())

max_cnt = 0
result = []

for house in houses:
    # 집과 사무실의 거리
    distance = house[1] - house[0]

    if distance <= railway:
        heappush(result, house[0])

    while result:
        temp = heappop(result)

        # 길이에 포함된다면, 다시 넣음
        if temp >= house[1] - railway:
            heappush(result, temp)
            break

    max_cnt = max(max_cnt, len(result))

print(max_cnt)