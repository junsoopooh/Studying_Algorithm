N = int(input())
stars = [[' ' for _ in range(2**N)] for _ in range(2**N)]

def fill_star(n, x, y):
    if n == 1:
        stars[x][y] = '*'
        return
    
    length = 2**N
    for i in range(length):
        stars[x][y+i] = '*'
        stars[x+i][y] = '*'
    
    fill_star(n-1, x+2, y+2)

fill_star(N, 0, 0)

for s in stars:
    print(''.join(s))
N = int(input())
board = [['' for _ in range(2**N)] for _ in range(2**N)]

def func(x, y, size):
    if (size == 1):
        board[x][y] = '*'
        return
    
    size /= 2
    func(x, y, size)
    func(x, y + size, size)
    func(x + size, y, size)
