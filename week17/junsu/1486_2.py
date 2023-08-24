import sys
from heapq import heappop, heappush

n, m, t, d = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
    'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def change(x):
    ans = alphabet.index(x)
    return ans


for i in range(n):
    for j in range(m):
        graph[i][j] = change(graph[i][j])

da = [0, -1, 0, 1]
db = [1, 0, -1, 0]


def search(p, q):
    time = [[10**9 for _ in range(m)] for _ in range(n)]
    time[p][q] = 0

    arr = []
    heappush(arr, [0, p, q])
    while arr:
        x, a, b = heappop(arr)

        if time[a][b] < x:
            continue

        for i in range(4):
            na = a + da[i]
            nb = b + db[i]
            if na >= 0 and na < n and nb >= 0 and nb < m:

                start = graph[a][b]
                arrive = graph[na][nb]
                dif_height = arrive - start

                if abs(dif_height) <= t:
                    if dif_height > 0:
                        current_time = x + (dif_height)**2
                    else:
                        current_time = x + 1

                    if time[na][nb] > current_time:
                        time[na][nb] = current_time
                        heappush(arr, [current_time, na, nb])

    return time


go_time = search(0, 0)
ans = []

for i in range(n):
    for j in range(m):
        if go_time[i][j] < d:
            heappush(ans, [-1*graph[i][j], i, j])

k = len(ans)
for i in range(k):
    h, a, b = heappop(ans)
    h *= -1
    back_time = search(a, b)
    total = back_time[0][0] + go_time[a][b]
    if total <= d:
        print(h)
        break
