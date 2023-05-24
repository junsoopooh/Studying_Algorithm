import sys

n,m = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

left = 0
right = max(trees) # 정렬후 인덱스로 지정안해도 된다.
ans = []

while left<=right:
    total = 0
    mid = (left+right)//2
    for i in trees:
        if i > mid: 
            total += (i-mid)
    
    if total == m:
        ans.clear()
        ans.append(mid)
        break
    elif total > m:
        ans.append(mid)
        left = mid+1
    else:
        right = mid-1

print(max(ans))

# 왜 오답처리될까?
# import sys

# n,m = map(int,sys.stdin.readline().split())
# trees = list(map(int,sys.stdin.readline().split()))

# left = 0
# right = max(trees)
# ans = 1

# while left<=right:
#     total = 0
#     mid = (left+right)//2
#     for i in trees:
#         if i > mid: 
#             total += (i-mid)
    
#     if total == m:
#         ans = mid
#         break
#     elif total > m:
#         ans = max(ans,mid)
#         left = mid+1
#     else:
#         right = mid-1

# print(ans)
