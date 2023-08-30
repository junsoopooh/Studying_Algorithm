import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
buildings = []
for _ in range(n):
    l,h,r = map(int,sys.stdin.readline().split())
    heappush(buildings,[l,h,r])
arr = []
ans = []
x = 0
h = 0
lim = 0
while buildings:
    tmp = heappop(buildings) # 빌딩 선정
    if not arr: # 아직 그려진 스카이라인이 없음
        ans.append(tmp[0]) # 지금 들어온 빌딩의 왼쪽
        ans.append(tmp[1]) # 지금 들어온 빌딩의 높이
        ans.append(tmp[2]) # 지금 들어온 빌딩의 오른쪽(새로운 빌딩 나타나지 않을 경우를 대비)
        ans.append(0) # 끝나면 높이는 다시 0으로 바뀜
        h = tmp[1]
        lim = tmp[2]
        heappush(arr,[-tmp[1],tmp[2]])
        continue
    if tmp[0] < lim: # 선정한 빌딩의 왼쪽 좌표가 이전 빌딩의 오른쪽좌표보다 먼저 나타남
        ans.pop() # 설정해둔 오른쪽좌표와 높이 0 삭제
        ans.pop() # 설정해둔 오른쪽좌표와 높이 0 삭제
    

    
    heappush(arr,[-tmp[1],tmp[2]]) # 빌딩 heap에 저장



    if ans[-1] < -arr[0][0]: # 최대힙을 통한 빌딩의 높이가 
        ans.append(tmp[0])
        ans.append(tmp[1])
        ans.append(tmp[2])
        ans.append(0)
print(ans)