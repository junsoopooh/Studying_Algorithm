import sys

n, b = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))


def solve(p,q): #곱하는 함수 만들기 (제곱 만들라했는데, 제곱 나누다보면 한번 곱해야할수도있어서..)
    k = len(p)
    new = [[0 for _ in range(k)] for _ in range(k)]
    for a in range(k):
        for b in range(k):
            tmp = 0
            for i in range(k):
                tmp += p[a][i]*q[i][b]
            new[a][b] = tmp%1000
    return new


def recur(p,x):
    if x == 1:
        for a in range(n):
            for b in range(n):
                p[a][b] %= 1000
        return p
    else: # 다제곱은 나눠야 제맛
        ans = recur(p,x//2)
        if x%2 == 1:
            return solve(solve(ans,ans),p)
        else:
            return solve(ans,ans)

result = recur(matrix, b)
for i in result:
    print(*i,end='\n')

