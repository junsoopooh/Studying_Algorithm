import sys

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

def moo(k):
    if k == 0:
        return 'moo'
    return moo(k-1)+'m'+'o'*(k+2)+moo(k-1)
i = -1
while True:
    i += 1
    tmp = moo(i)
    if len(tmp) >= n:
        print(tmp[n-1])
        break

