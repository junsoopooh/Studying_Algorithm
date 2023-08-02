import sys
input = sys.stdin.readline

def solve(index, top, bottom):
    top = values[index] * bottom + top
    bottom = bottom

    if index < 1:
        print(f'{top}/{bottom}')
        return
    else:
        solve(index-1, bottom, top)

n = int(input())
values = list(map(int, input().split()))

if len(values) == 1:
    print(values[0])
else:
    solve(n-2, 1, values[-1])