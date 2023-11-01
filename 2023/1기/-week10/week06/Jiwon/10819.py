import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
values = list(map(int, input().split()))

maxvalue = 0

for value in permutations(values, n):
    orders = list(value)
    sumvalue = 0
    
    # 인덱스가 넘어감으로 n-1로 변경
    for i in range(n-1):
        sumvalue += abs(orders[i] - orders[i+1])

    maxvalue = max(maxvalue, sumvalue)

print(maxvalue)