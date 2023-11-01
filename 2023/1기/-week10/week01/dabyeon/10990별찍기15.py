import sys
input = sys.stdin.readline

N = int(input().rstrip())

# for i in range(N):
#     if i == 0:
#         print(" "*(N-1) + "*")
#     else:
#         print(" "*(N-i-1) + "*" + " "*(2*i-1)+ "*" + " "*(N-i-1))

def recursion(n, i=0):
    if n < 1:
        return
    else:
        if i == 0:
            print(" "*(N-1) + "*")
        else: 
            print(" "*(N-i-1) + "*" + " "*(2*i-1)+ "*")
        return recursion(n-1, i+1)

recursion(N)