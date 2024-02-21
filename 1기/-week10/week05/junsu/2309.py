import sys

arr = []
sum = 0
visited = [False]*9
fake = []
for _ in range(9):
    height = int(sys.stdin.readline())
    arr.append(height)
    sum += height


def dfs(x, num):
    if x == 0:
        if num == 100:
            return
    else:
        for i in range(9):
            if visited[i] == False:
                num -= arr[i]
                x -= 1
                visited[i] = True
                if num >= 100:
                    fake.append(arr[i])
                    dfs(x, num)
                    num += arr[i]
                    x += 1
                    visited[i] = False
                    fake.remove(arr[i])
                else:
                    x += 1
                    num += arr[i]


dfs(2, sum)
print(fake)
