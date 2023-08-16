#DFS with recursion
import sys
from collections import deque
input=sys.stdin.readline

N, M =map(int,input().split())

bigger_lst=[[] for _ in range(N+1)]  # index보다 큰 수
smaller_lst=[[] for _ in range(N+1)]  # index보다 작은 수
mid=(N+1)/2 #개수 기준 중간값

for i in range(M):  #값 입력후 배열
    a,b=map(int,input().split())
    bigger_lst[b].append(a)
    smaller_lst[a].append(b)

def dfs(arr, n):   #bigger, smaller, list보고 n보다 크거나 작은 숫자 개수 파악
    global cnt
    for i in arr[n]:
        if not visited[i]:
            visited[i]=True
            cnt+=1
            dfs(arr,i)

answer=0
for i in range(1,N+1):
    visited=[False]*(N+1)
    cnt=0
    dfs(bigger_lst,i)
    if cnt>=mid:
        answer+=1
    cnt=0
    dfs(smaller_lst,i)
    if cnt>=mid:
        answer+=1

print(answer)