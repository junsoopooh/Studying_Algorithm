import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    x,r = map(int,sys.stdin.readline().split())
    arr.append([x+r,x-r])
arr.sort(key = lambda x : x[1])
graph = [0 * (2*n+1)]
cnt = 0
graph[1] = arr[0][1]

