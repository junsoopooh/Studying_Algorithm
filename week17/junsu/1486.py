import sys
from collections import deque

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


time = [[[0, 0] for _ in range(m)] for _ in range(n)]

da = [0, -1, 0, 1]
db = [1, 0, -1, 0]
arr = deque()
arr.append([0, 0])
height = 0
while arr:
    a, b = arr.popleft()
    for i in range(4):
        updated = False
        na = a + da[i]
        nb = b + db[i]
        if na >= 0 and na < n and nb >= 0 and nb < m:
            if not na and not nb:
                continue
            arrive = graph[na][nb]
            start = graph[a][b]

            dif_height = change(arrive) - change(start)
            if abs(dif_height) > t:
                continue

            if dif_height > 0:
                current_time_go = dif_height**2
                current_time_back = 1
            else:
                current_time_go = 1
                current_time_back = dif_height**2

            current_time_go += time[a][b][0]
            current_time_back += time[a][b][1]

            if not time[na][nb][0] or current_time_go < time[na][nb][0]:
                time[na][nb][0] = current_time_go
                updated = True

            if not time[na][nb][1] or current_time_back < time[na][nb][1]:
                time[na][nb][1] = current_time_back
                updated = True

            if updated:
                arr.append([na, nb])
            if time[na][nb][0] + time[na][nb][1] <= d:
                height = max(height, change(graph[na][nb]))

print(height)
