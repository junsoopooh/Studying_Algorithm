# import sys

# def dfs(start, now, value, cnt):
#     global ans
#     if cnt == N:
#         if a[now][start]:
#             value += a[now][start]
#             if ans > value:
#                 ans = value
#         return
#     if value > ans:
#         return
    
#     for i in range(N):
#         if not visited[i] and a[now][i]:
#             visited[i] = 1
#             dfs(start, i, value + a[now][i], cnt + 1)
#             visited[i] = 0


# N = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# # print(w)
# ans = sys.maxsize
# visited = [0] * N
# for i in range(N):
#     visited[i] = 1
#     dfs(i, i, 0, 1)
#     visited[i] = 0
# print(ans)

### 다른 풀이 ###
import sys
N = int(input()) #도시의 개수
travel_cost = [list(map(int, input().split())) for _ in range(N)]
min_value = sys.maxsize #출력할 최소값 정의

def dfs_backtracking(start, next, value, visited): #시작도시번호, 다음도시번호, 비용, 방문 도시
    global min_value

    if len(visited) == N: #만약 방문한 도시가 입력받은 도시의 개수라면
        if travel_cost[next][start] != 0: #마지막 도시에서 출발 도시로 가는 비용이 0이 아니라면(즉, 갈수 있다면)
            min_value = min(min_value, value + travel_cost[next][start]) #더한 값을 저장되어있는 최소값과 비교해서 대입
        return
    for i in range(N): #도시의 개수 만큼 반복문을 돈다.
        #만약 현재 도시에서 갈 수 있는 도시의 비용이 0이 아니고 이미 방문한 도시가 아니며 그 비용값이 저장되어 있는 최소값 보다 작다면
        if travel_cost[next][i] != 0 and i not in visited and value < min_value:
            visited.append(i) # 그 도시를 방문목록에 추가
            dfs_backtracking(start, i, value + travel_cost[next][i], visited) # 그 도시를 방문한다.
            visited.pop() # 방문을 완료했다면 방문목록 해제

#도시마다(0~3) 출발점을 지정
for i in range(N):
    dfs_backtracking(i, i, 0, [i])
print(min_value)