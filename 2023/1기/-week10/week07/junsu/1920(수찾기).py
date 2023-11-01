import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
A.sort()
m = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

for x in nums:
    left = 0
    right = n-1
    ans = 0
    while left <= right:
        mid = (left+right)// 2
        key = A[mid]
        if x == key:
            ans = 1
            break
        if x > key:
            left = mid + 1
        elif x < key:
            right = mid - 1
    print(ans)

        




# 시간초과 답
# for x in nums:
#     if A.count(x) == 0:
#         print(0)
#     else:
#         print(1)
