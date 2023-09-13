import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

values = list(str(a*b*c))

for i in range(10):
    print(values.count(str(i)))