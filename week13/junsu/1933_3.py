import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
buildings = [] # 빌딩들을 담을 배열
heights = [0] * n # 빌딩의 높이를 담을 배열
ends = [0] * n # 빌딩의 오른쪽 점을 담을 배열
heap = [] 
arr = set() # 지나간 끝점들을 저장해둘 배열
for i in range(n):
    l,h,r = map(int,sys.stdin.readline().split())
    buildings.append([l,i,1]) # 시작점이라면 좌표와 index, 1을 저장
    buildings.append([r,i,0]) # 끝점이라면 좌표와 index, 0을 저장
    heights[i] = h # index로 높이 저장
    ends[i] = r # index로 끝점 저장

#빌딩들을 정렬한다. 먼저 시작하는 순서대로, 그 다음은 시작점이 먼저 오도록, 그다음은 높이가 높은 순서대로.
buildings.sort(key=lambda x: (x[0], -x[2], -heights[x[1]]))

h = 0 # 최고높이 저장 변수
ans = [] # 정답을 담아둘 배열

# 여기 범위를 n으로 하면 안되는 이유 : 시작점 끝점 나눴으니 n의 2배가 buildings의 길이
for i in range(len(buildings)):
    point, index, flag = buildings[i] # 각각 좌표, index, 시작점인지 끝점인지 나타내는 flag

    if flag == 1: # 시작점이라면?
        if h < heights[index]: # 현재 최고 높이보다 크다면?
            h = heights[index] # 새롭게 업데이트
            ans.append((point,h)) # 스카이라인이 변경되었으니 정답 배열에 추가
        heappush(heap,(-heights[index],ends[index])) # heap에 높이와 끝점을 추가한다. 최대heap을 위해 음수로 저장
    else: # 끝점이라면?
        arr.add(point) # 끝점을 만났으니 이 좌표는 담아둔다.
        while heap: # heap이 비어 있지 않다면 반복한다.
            if heap[0][1] not in arr: # 최대높이 빌딩의 끝점이 set에 없다면? => 아직 끝점을 만나지 않은 빌딩이라면?
                break # 검사를 멈춘다.
            heappop(heap) # set에 있다면 이미 끝난 빌딩이므로 제거한다.
        if not heap: # 현재 스카이라인을 그릴 빌딩이 없다면?
            if h:
                h = 0 # 현재 높이 0으로 업데이트
                ans.append((point, h)) # 업데이트되었으니 정답 배열에 추가
        else: # 스카이라인을 그릴 빌딩이 있다면?
            if -heap[0][0] != h: # 기존의 최고높이 빌딩이 아니라면
                h = -heap[0][0] # 새로운 최고 높이 업데이트
                ans.append((point, h)) # 정답 배열에 추가
for i in ans:
    print(i[0], i[1], end=' ') # 업데이트 될때마다 정답배열에 추가했으니 각각 출력한다.