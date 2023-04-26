
import sys
n = int(sys.stdin.readline())
# n개의 원반을 a -> c로 이동
def Hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
        return

    # 원반 n-1 b로 이동
    Hanoi(n-1, a, c, b)
    # 가장 큰 원반을 c 로 이동
    print(a, c)
    # b 에 있는 원반 n-1 개를 c로 이동
    Hanoi(n-1, b, a, c)

print(2 ** n - 1) # 이동 횟수
if n <= 20: Hanoi(n, 1, 2, 3)

#나의 답(메모리 초과)
# import sys

# n = int(sys.stdin.readline())
# arr = []

# def tower(a,b,x):
#     if x == 1:
#         arr.append([a,b])
#         return arr
    
#     elif x == 2:
#         arr.append([a,6-a-b])
#         arr.append([a,b])
#         arr.append([6-a-b,b])
#         return arr
    
#     elif x == 3:
#         arr.append([a,b])
#         arr.append([a,6-a-b])
#         arr.append([b,6-a-b])
#         arr.append([a,b])
#         arr.append([6-a-b,a])
#         arr.append([6-a-b,b])
#         arr.append([a,b])
#         return arr

#     else:
#         tower(a,6-a-b,x-1)
#         arr.append([a,b])
#         tower(6-a-b,b,x-1)
#         return arr
    
# def big(x):
#     if x == 1:
#         return 1
#     elif x == 2:
#         return 3
#     elif x == 3:
#         return 7
#     else:
#         return 2*big(x-1) +1

# tower(1,3,n)

# if n <= 20:    
#     print(len(arr))
#     for i in arr:
#         print(*i,end ='\n',sep=' ')

# else:
#     ans = big(n)
#     print(ans)
