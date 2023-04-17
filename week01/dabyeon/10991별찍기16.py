import sys
input = sys.stdin.readline

N = int(input().rstrip())

def recursion(n, i=0):
    if n < 1:
        return
    else:
        if i == 0:
            print(" "*(N-1) + "*")
        else: 
            print(" "*(N-i-1) + "* "*i + "*")
        return recursion(n-1, i+1)

recursion(N)