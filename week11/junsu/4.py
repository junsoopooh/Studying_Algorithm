# 배달

# 오답 코드

from collections import deque

def solution(N, road, K):
    board = [[False for _ in range(N)] for _ in range(N)]
    for a,b,t in road:
        if not board[a-1][b-1]:
            board[a-1][b-1] = t
        else:
            board[a-1][b-1] = min(board[a-1][b-1],t)    
        if not board[b-1][a-1]:
            board[b-1][a-1] = t
        else:
            board[b-1][a-1] = min(board[b-1][a-1],t)    
    
    answer = 0
    checked = [False for _ in range(N)]
    checked[0] = True
    q = deque()
    q.append([0,0])
    while q:
        now, time = q.popleft()
        for i in range(N):
            if not checked[i] and board[now][i]:
                if time + board[now][i] <= K:
                    checked[i] = True
                    q.append([i,time+board[now][i]])
    answer = checked.count(True)
    return answer

# 정답 코드

from heapq import heappop, heappush
def solution(N, road, K):
    answer = 0
    
    def search(distance,tmp):
        q = []
        heappush(q,[0,1])
        while q:
            cnt, now = heappop(q)
            for time, next_node in tmp[now]:
                if cnt + time < distance[next_node]:
                    distance[next_node] = cnt + time
                    heappush(q,[cnt+time,next_node])

    distance = [500001 for _ in range(N+1)]
    distance[1] = 0
    tmp = [[] for _ in range(N+1)]
    for a,b, t in road:
        tmp[a].append([t,b])
        tmp[b].append([t,a])
        
    search(distance,tmp)
    
    return len([i for i in distance if i <=K])
