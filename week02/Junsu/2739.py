import sys

n = int(sys.stdin.readline())

for i in range(1,10):
    list = [n,'*',i,'=',n*i]
    print(*list, sep=' ')
