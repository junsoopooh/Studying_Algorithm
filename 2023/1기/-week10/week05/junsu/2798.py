import sys

n,m = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
visited = [False]*n
arr = []

def dfs(x,sum):
    if x == 0:
        if sum <= m:
            arr.append(sum)
    else:
        for i in range(len(cards)):
            if visited[i] == False:
                sum += cards[i]
                visited[i] = True
                x -= 1
                if sum <= m:
                    dfs(x,sum)
                    sum -= cards[i]
                    visited[i] = False
                    x += 1
                else:
                    x += 1
                    sum -= cards[i]
                    visited[i] = False
dfs(3,0)
print(max(arr))


