import sys

T = int(sys.stdin.readline())

# 썼지만 시간초과로 틀린 코드
# for _ in range(T):
#     n = int(sys.stdin.readline())
#     def prime(x):
#         if x == 2:
#             return 1
#         elif x == 3:
#             return 1
#         elif x == 4:
#             return False
#         else:
#             for i in range(2,x):
#                 if x%i == 0:
#                     return False
#             return 1

#     for j in range(2,n//2):
#         if prime(j) == 1 and prime(n-j) == 1:
#             ans = [j,n-j]
#     print(*ans, sep=' ')

def prime(x):
    if x == 1:
        return False
    else:
        for i in range(2,int(1+x**0.5)):
            if x%i == 0:
                return False
        return True

for _ in range(T):
    n = int(sys.stdin.readline())
    a = b = n//2
    while a>0:
        if prime(a) and prime(b):
            ans = [a,b]
            print(*ans, sep=' ')
            break
        else:
            a -= 1
            b += 1