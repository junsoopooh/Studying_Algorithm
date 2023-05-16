# 백트래킹
import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)

# N = int(input())
# a = list(map(int, input().split()))

### 다시 풀어보기 ###
# import sys
# input = sys.stdin.readline
# num = list(map(int, input().split()))
# op = list(map(int, input().split()))

# maximun = -1e9
# minimum = 1e9

# def dfs(depth, total, plus, minus, multi, div):
#     global maximum, minimum
#     if depth == N:
#         maximum = max(total, maximum)
#         minimum = min(total, minimum)
#         return
#     else:
#         if plus >= 1:
#             dfs(depth+1, total += num[depth], plus-1, minus, multi, div)
#         if minus >= 1:
#             dfs(depth+1, total -= num[depth], plus, minus-1, multi, div)
#         if multi >= 1:
#             dfs(depth+1, total * num[depth], plus, minus, multi-1, div)
#         if div >= 1:
#             dfs(depth+1, int(total / num[depth]), plus, minus, multi, div-1)
# dfs(1, num[0], op[0], op[1], op[2], op[3])
