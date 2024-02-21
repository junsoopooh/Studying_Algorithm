# 0번째: 0
# 1번째: 1
# 2번째: 0 + 1
# 3번째: 1 + 1
# 4번째: 1 + 2
# 5번째: 2 + 3
# import sys
# input = sys.stdin.readline
# def fibonachi(n):
#   if n == 0:
#     return 0
#   elif n == 1:
#     return 1
#   elif n > 1:
#     return fibonachi(n-1) + fibonachi(n-2)

# print(fibonachi(int(input())))

n = int(input())

def fibo_dp(num):
  cache = [0 for _ in range(num + 1)]
  cache[0] = 0
  cache[1] = 1

  for i in range(2, num+1):
    cache[i] = cache[i-1] + cache[i-2]
  return cache[num]
print(fibo_dp(n))