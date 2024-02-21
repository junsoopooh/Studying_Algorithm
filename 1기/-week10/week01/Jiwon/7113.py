import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 9)

def rectangle(n, m):
    global count

    if n < m:
        count += 1
        temp = m-n
        rectangle(n, temp)

    elif n > m:
        count += 1
        temp = n-m
        rectangle(temp, m)
    
    else:
        count += 1
        return


n, m = map(int, input().split())

count = 0
rectangle(n, m)

print(count)