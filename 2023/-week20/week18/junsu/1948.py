import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
level = [0 for _ in range(n+1)]
for _ in range(m):
    a,b,t = map(int,sys.stdin.readline().split())
    graph[a].append([b,t])
    level[b] += 1
start, arrive = map(int,sys.stdin.readline().split())

arr = deque()
arr.append(start)
        
cnt = 0
ans = 0
while arr:
    now = arr.popleft()
    cnt += 1
    if now == arrive:
        break
    for i in graph[now]:
        next = i[0] 
        time = i[1]
        level[next] -= 1
        if not level[next]:
            arr.append(next)
            ans += time

print(cnt)
print(ans)