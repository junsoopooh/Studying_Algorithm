'''
10
0
1  0
1
0  1
2
1  1
3
1  2
4
2  3
5
3  5
6
5  8
7
8  13
8
13  21
9
21  34
'''

T = int(input())

for _ in range(T):
    N = int(input())
    dpZero = [0] * (N+1)
    dpOne = [0] * (N+1)

    if N == 0:
        dpZero[0],dpOne[0] = 1,1
        print("1 0")
    else:
        dpZero[0],dpZero[1] = 1,0
        dpOne[0],dpOne[1] = 0,1

        for i in range(2,N+1):
            dpZero[i] = dpZero[i-1] + dpZero[i-2]
            dpOne[i] = dpOne[i-1] + dpOne[i-2]
        print(dpZero[N],dpOne[N])
