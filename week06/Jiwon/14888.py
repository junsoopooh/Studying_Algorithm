import sys
input = sys.stdin.readline

maxvalue = ~sys.maxsize
minvalue = sys.maxsize

def solve(depth, value, plus, minus, multiple, divide):
    global maxvalue, minvalue

    if depth == n:
        maxvalue = max(maxvalue, value)
        minvalue = min(minvalue, value)
        return

    if plus:
        solve(depth+1, value+values[depth], plus-1, minus, multiple, divide)
    if minus:
        solve(depth+1, value-values[depth], plus, minus-1, multiple, divide)
    if multiple:
        solve(depth+1, value*values[depth], plus, minus, multiple-1, divide)
    if divide:
        solve(depth+1, int(value/values[depth]), plus, minus, multiple, divide-1)

# 수의 개수
n = int(input())

# 수 리스트
values = list(map(int, input().split()))

# 연산자 개수
plus, minus, multiple, divide = map(int, input().split())

solve(1, values[0], plus, minus, multiple, divide)

print(maxvalue)
print(minvalue)