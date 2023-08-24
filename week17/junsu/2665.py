import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

da = [0, -1, 0, 1]
db = [1, 0, -1, 0]


def search(p, q):
    cnt = [[10**9 for _ in range(n)] for _ in range(n)]
    cnt[p][q] = 0
    arr = []
    heappush(arr, [0, p, q])
    while arr:
        cost, a, b = heappop(arr)
        for i in range(4):
            na = a + da[i]
            nb = b + db[i]
            if na < 0 or na > n-1 or nb < 0 or nb > n-1:
                continue
            if board[na][nb] == '0':
                new_value = cost + 1
            else:
                new_value = cost

            if cnt[na][nb] == 10**9:
                cnt[na][nb] = new_value
                heappush(arr, [new_value, na, nb])
            else:
                if new_value < cnt[na][nb]:
                    cnt[na][nb] = new_value
                    heappush(arr, [new_value, na, nb])
    return cnt


ans = search(0, 0)
print(ans[n-1][n-1])
