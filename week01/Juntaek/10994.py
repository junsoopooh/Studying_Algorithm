# def starN(n):
#     for _ in range(n):
#         print('')
#         for _ in range(n):
#             print('*', end='')

# starN(5)

# starN이라는 함수 안에서 또 함수를 부르는 방법.
# 한놈은 일자로만 찍고 한놈은 띄어쓰기로 찍고?

# 풀이 코드
# N = int(input())
# stars = [[' ' for _ in range(4 * N - 3)] for _ in range(4 * N -3)]
# print(stars)

# def fill_star(n, x, y):
#     if n == 1:
#         stars[y][x] = '*'
#         return
    
#     length = 4 * n - 3

#     for i in range(length):
#         stars[y][x+i] = '*'
#         stars[y + i][x] = '*'
#         stars[y + length - 1][x + i] = '*'
#         stars[y + i][x + length - 1] = '*'
    
#     fill_star(n - 1, x + 2, y + 2)

# fill_star(N, 0, 0)
# for s in stars:
#     print(''.join(s))

# 다시 풀어보기
import sys
sys.setrecursionlimit(10**7)

N = int(input())
# length = 4 * N - 3
stars = [[' ' for _ in range(4 * N - 3)] for _ in range(4 * N - 3)]
# print(stars)

def fill_stars(n, x, y):
    if n == 1:
        stars[x][y] = '*'
        return
    # else:
    length = 4 * n - 3
    for i in range(length):
        stars[x][y + i] = '*'
        stars[x + i][y] = '*'
        stars[x + length -1][y + i] = '*'
        stars[x + i][y + length -1] = '*'
        # stars[y][x+i] = '*'
        # stars[y + i][x] = '*'
        # stars[y + length - 1][x + i] = '*'
        # stars[y + i][x + length - 1] = '*'
    
    fill_stars(n-1, x+2, y+2)

fill_stars(N, 0, 0)

# for _ in range(length):
#     print(''.join(stars))
for s in stars:
    print(''.join(s))
# print(stars)