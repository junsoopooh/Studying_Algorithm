import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    R, S = input().rstrip().split()

    result = ""
    for e in S:
        result += e * int(R)
    
    print(result)