import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 건물의 수
n = int(input())

# 건물 정보를 저장할 리스트
buildings = []

# 각 건물의 끝나는 지점을 저장할 리스트
end_points = []

for i in range(n):
    l, h, r = map(int, input().split())

    # [인덱스, 시작점, 높이, 0]
    buildings.append([i, l, h, 0])

    # [인덱스, 끝점, 높이, 1]
    buildings.append([i, r, h, 1])

    # 현재 건물의 끝나는 지점을 저장
    end_points.append(r)

# 시작점 기준으로 정렬
# 시작점이 같은 경우 시작점이 끝점보다 먼저 오도록
# 높은 건물이 우선 처리되어 윤곽선에 영향을 미치도록
buildings.sort(key=lambda x: (x[1], x[3], -x[2]))

curr_height = 0
end_list = set()

results = []
not_ended_buildings = []

for building in buildings:
    # 인덱스, X 좌표 (시작점/끝점), 높이, 끝나는 지점
    building_idx, building_x, building_height, building_end = building

    # 시작점인 경우
    if not building_end:
        # 현재 높이 < 건물 높이
        # 현재 높이를 건물의 높이로 업데이트 해야지
        if curr_height < building_height:
            curr_height = building_height
            results.append([building_x, curr_height])

        # 현재 건물의 높이, 끝나는 X 좌표 힙에 저장
        heappush(not_ended_buildings, [-building_height, end_points[building_idx]])
        continue

    # 끝점인 경우
    end_list.add(building_x)

    # 끝난 건물은 힙에서 삭제
    while not_ended_buildings and not_ended_buildings[0][1] in end_list:
        heappop(not_ended_buildings)

    # 진행중인 건물이 있다면 현재 높이 업데이트
    if not_ended_buildings:
        if curr_height != -not_ended_buildings[0][0]:
            curr_height = -not_ended_buildings[0][0]
            results.append([building_x, curr_height])

    # 진행중인 건물이 없으면 현재 높이 0으로
    else:
        if curr_height != 0:
            curr_height = 0
            results.append([building_x, curr_height])

for result in results:
    print(' '.join([str(result[0]), str(result[1])]), end=' ')