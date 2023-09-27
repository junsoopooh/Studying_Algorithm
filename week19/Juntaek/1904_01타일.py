# 0이라는 낱장의 타일을 붙여서 00타일들로 만듬
# 현재 1 or 00타일들만이 존재
# 1일때 1 : 1개
# 2일때 00, 11 : 2개
# 3일때는 100, 111, 001 : 3개
# 4일때 0011, 0000, 1001, 1100, 1111 : 5개
# 5일때 00111, 10011, 11001, 11100, 00100, 00001, 10000, 11111
# 결국 f(n) = f(n-1) + f(n-2)
import sys
input = sys.stdin.readline

n = int(input())

def DP(n):
  cache = [0] * (n+1) # 이렇게 하면 indexError..
  # if n == 1: cache[n] = 1 이런식으로 코트를 짜야 indexError를 잘 해결할 수 있음
  cache[1] = 1
  cache[2] = 2
  for i in range(3, n+1):
    cache[i] = cache[i-1] + cache[i-2] # 애초에 큰 값이 들어가면 메모리가 초과되니까 그걸 줄여줄려고 나머지 값을 캐시에 미리 넣어주는 거임
  return cache[n] % 15746 # 이렇게 하면 메모리 초과

print(DP(n))