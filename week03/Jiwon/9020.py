import sys
input = sys.stdin.readline

# 0과 1은 소수에서 제외, 
prime = [0, 0] + [1] * 10002

for i in range(2, 10002):
    if prime[i]:
        for j in range(2*i, 10002, i):
            prime[j] = 0

# 테스트 케이스 수
t = int(input())

for i in range(t):
    n = int(input())

    a, b = n//2, n//2

    while a > 0:
        if prime[a] and prime[b]:
            print(a, b)
            break
        else:
            a-=1
            b+=1