import sys
input = sys.stdin.readline

# 한 변의 길이 n
n = int(input())

# 하얀색 0, 파란색 1
values = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def solve(x, y, len):
    global white, blue

    # 현재 좌표의 컬러
    now = values[x][y]

    for i in range(x, x+len):
        for j in range(y, y+len):
            # 만약 다르다면,
            if now != values[i][j]:
                # 반으로 나눠 다시 들어가봐야지
                half = len//2

                solve(x, y, half)
                solve(x+half, y, half)
                solve(x, y+half, half)
                solve(x+half, y+half, half)

                return
            
    if now == 0:
        white += 1
    else:
        blue += 1

solve(0, 0, n)
print(white, blue, sep="\n")