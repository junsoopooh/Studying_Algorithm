import sys

n = int(sys.stdin.readline()) 
matrix = [] # 행렬 형태 받기
for _ in range(n):
    matrix.append(list(map(int,sys.stdin.readline().split())))
visited = [False]*(n) # 방문 표시
tmp = [] # 각 dfs마다 계산된 결과를 저장할 리스트

def dfs(now,city,cost):
    global start # 첫 출발지를 저장해둬야 마지막에 돌아오는 비용을 확인하고 더 해줄 수 있음

    if city == n: # 모든 도시를 순회했고
        if matrix[now][start]: # 마지막 도착 지점에서 출발지까지 가는 방법이 있다면
            cost += matrix[now][start] # 그 비용을 더해주고
            tmp.append(cost) # 결과 저장 리스트에 삽입
            return # 함수를 종료한다.
    else: # 아직 모든 도시를 순회 못했다면?
        for i in range(1,n): 
            if not visited[i] and matrix[now][i]: # i가 아직 방문하지 않은 도시고, 여기서 i까지 갈 방법이 있다면?
                cost += matrix[now][i] # 비용을 더해주고
                visited[i] = True # 방문처리
                city += 1 # 방문한 도시 수 1 증가
                dfs(i,city,cost) # 혹시 이 밑 과정이 백트래킹이라는건가?
                cost -= matrix[now][i] # 다음 경우 탐색을 위해 비용 다시 감소
                visited[i] = False # 방문처리 취소
                city -= 1 # 방문한 도시 수 원상복구

arr = []
for i in range(n):
    visited[i] = True # i에서 출발하니 중간에 i로 안오도록 방문처리
    start = i # 출발지를 저장해둔다.
    dfs(i,1,0)
    arr.append(min(tmp)) # dfs로 나온 결과를 저장한 tmp에서 최솟값을 찾아 arr에 따로 저장한다.
print(min(arr))  # arr에는 출발지 별 최소 비용이 저장되 있으니 그중 최솟값을 찾아 출력
