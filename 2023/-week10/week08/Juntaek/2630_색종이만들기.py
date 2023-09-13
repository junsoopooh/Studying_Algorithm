# #잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램
# # 0은 하얀색, 1은 파란색
# # n이 주어졌을 때 모두 같은 색으로 칠해져 있다면? 그냥 cnt += 1하고 종료하면돼
# # 그런데 모두 같은 색이 아니라면? n/2로 나누자!
# # 각각 n/2만큼을 다 파악해봤는데 사분면 각각을 체크해서 모두 같은 색이다? 그러면 그 색에 맞게 카운트 해주기!


### 다시 풀어보기 ###
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
result = []
def sol(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(x, x+n):
            if paper[i][j] != color:
                sol(x, y, n//2)
                sol(x, y+n//2, n//2)
                sol(x+n//2, y, n//2)
                sol(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)
    # result.append(color)
sol(0, 0, N)
print(result.count(0))
print(result.count(1))
