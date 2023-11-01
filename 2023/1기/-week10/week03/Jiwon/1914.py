import sys
input = sys.stdin.readline

def Hanoi (n, a, b, c):
  if (n == 1):
    print(a, c, sep=" ")
  else:
    Hanoi(n-1, a, c, b)
    Hanoi(1, a, b, c)
    Hanoi(n-1, b, a, c)

# 원판의 개수 n
n = int(input())

# 옮긴 횟수 k
print(2**n - 1)

# n이 20보다 큰 경우에는 출력 X
if (n <= 20):
  Hanoi(n, 1, 2, 3)