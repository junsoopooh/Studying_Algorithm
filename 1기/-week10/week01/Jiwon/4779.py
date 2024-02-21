import sys
input = sys.stdin.readline

def solve(n):
    if n == 1:
        print('-', end='')
        return
    else:
        temp = n//3

        solve(temp)
        print(' ' * (n//3), end='')
        solve(temp)

while True:
    try:
        n = int(input().strip())

        if n == 0:
            print('-')
        else:
            solve(3 ** n)
            print()
    
    except:
        break