import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

visited = [False]*N
perm = []

# 중복 반문을 피하기 위해 start 파라미터 이용
# start 파라미터는 현재 노드 이후의 노드 중에서
# 탐색할 첫번째 노드의 인덱스 값!!!
# 이미 방문한 노드들을 모두 방문한 후에 
# 현재 노드에서 이후 노드들을 탐색하게 되어 중복 방문을 피할 수 있음

def dfs(m, start):
    if m == 0:
        print(*perm)
        return
    else:
        for i in range(start, N):
            if visited[i] == False:
                visited[i] = True
                perm.append(i+1)
                dfs(m-1, i+1)
                visited[i] = False
                perm.pop()

dfs(M, 0)