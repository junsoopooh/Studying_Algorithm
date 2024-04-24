#[별 찍기 - 10](https://www.acmicpc.net/problem/2447)
# 참고 : https://cotak.tistory.com/38

import sys

n = int(sys.stdin.readline())
board = [[' ' for _ in range(n)] for _ in range(n)]

def main(num:int):
    if num == 3:
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    board[i][j] = '*'
        return
    
    p = num//3
    main(p)

    for i in range(0, num, p):
        for j in range(0, num, p):
            if i != p or j != p:
                for x in range(p):
                    board[i+x][j:j+p] = board[x][:p]

main(n)
for i in range(n):
    for j in range(n):
        print(board[i][j], end='')
    print()