import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    prim = [1] + [0]*N
    prim[1] = 1 

    for i in range(2, int(N**0.5)+1):
        for j in range(i*i, N+1, i):
            # print(f'i : {i}, j : {j}')
            prim[j] = 1

    pair = []
    min_diff = float("inf")
    for i in range(2, N+1):
        if prim[i] == 0:
            if prim[N-i] == 0:
                diff = abs(i - (N-i))
                if diff < min_diff:
                    min_diff = diff
                    pair.append((i, N-i))

    print(*pair[-1])