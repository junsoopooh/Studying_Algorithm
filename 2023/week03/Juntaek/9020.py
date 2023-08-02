# 알단 소수를 구해야 하지 않을까?
# def is_prime():
#     if n == 1:
#     elif n >= 1:
#         for i in range(2, n):
#             if n % i == 0:
                
# 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다.

def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

for _ in range(int(input())):
    num = int(input())

    a, b = num//2, num//2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
        else:
            a -= 1
            b += 1