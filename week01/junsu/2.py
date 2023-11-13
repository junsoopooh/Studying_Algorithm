# 게임 맵 최단거리

from collections import deque

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])

    da = [1,-1,0,0]
    db = [0,0,1,-1]
    
    maps[0][0] = 0
    q = deque()
    q.append([0,0,0])
    
    while q:
        a,b,cnt = q.popleft()
        if a == n-1 and b == m-1:
            answer = cnt+1
            print(a,b)
            return answer
        for i in range(4):
            na = a + da[i]
            nb = b + db[i]
            if na < 0 or na >= n or nb < 0 or nb >= m or not maps[na][nb]:
                continue
            q.append([na,nb,cnt+1])
            maps[na][nb] = 0
    return answer