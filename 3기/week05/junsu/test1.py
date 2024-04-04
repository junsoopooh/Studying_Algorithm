# [소수경로](https://www.acmicpc.net/problem/1963)
import sys
from heapq import heappop, heappush

def check(k:int):
    if not k%2:
        return False
    for i in range(3,int(k**(0.5))+1):
        if not k%i:
            return False
    else:
        return True

prime_numbs = [ False for _ in range(10000)]
for i in range(1000,10000):
    if check(i):
        prime_numbs[i] = True

def change_num(arr: list):
    result = []
    for i in range(10):
        for j in range(4):
            # 여기가 핵심
            tmp = arr.copy()
            tmp[j] = str(i)
            if int("".join(tmp)) > 999 and prime_numbs[int("".join(tmp))] and tmp != arr:
                result.append(tmp)
    return result  

t = int(sys.stdin.readline())
for _ in range(t):
    answer = 'Impossible'
    a,b = map(int,sys.stdin.readline().split())
    visited = [False for _ in range(10000)]
    visited[a] = True

    q = []
    a_arr = list(str(a))
    b_arr = list(str(b))
    heappush(q,[0,a_arr])
    while q:
        cnt, now = heappop(q)
        if now == b_arr:
            answer = cnt
            break        
        change_arr = change_num(now)
        for num in change_arr:
            if not visited[int("".join(num))]:
                visited[int("".join(num))] = True
                heappush(q,[cnt+1, num])
    print(answer)