import sys
sys.setrecursionlimit(10**6)

n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    graph.append(arr)

da = [0,-1,0,1]
db = [1,0,-1,0]
melt = [[0 for _ in range(m)] for _ in range(n)]

def dfs(a,b):
    tmp = 0
    for i in range(4):
        new_a = a + da[i]
        new_b = b + db[i]
        if graph[new_a][new_b]:
            tmp += 1
    melt[a][b] = tmp

flag = False
def check(ice):
    global flag
    visited = [[False for _ in range(m)] for _ in range(n)]
    a,b = ice.pop()
    while ice:
        for i in range(4):
            new_a = a + da[i]
            new_b = b + db[i]
            if graph[new_a][new_b]:
                visited[a][b] = True
                ice.append([new_a,new_b])
                check(ice)
    
    for a in range(1,n-1):
        for b in range(1,m-1):
            if not visited[a][b] and graph[a][b]:
                flag = True
                return

cnt = 0
while True:
    cnt += 1
    ice = []
    for a in range(1,n-1):
        for b in range(1,m-1):
            if graph[a][b]:
                dfs(a,b)

    for a in range(1,n-1):
        for b in range(1,m-1):
            graph[a][b] -= melt[a][b]
            if graph[a][b] < 0:
                graph[a][b] == 0
            elif graph[a][b]:
                ice.append([a,b])

    if not ice:
        cnt = 0
        break
    else:
        check(ice)
        if flag:
            break

print(cnt)