# [랜선 자르기](https://www.acmicpc.net/problem/1654)

import sys

k,n = map(int,sys.stdin.readline().split())
lan = []
for _ in range(k):
    lan.append(int(sys.stdin.readline()))

low = 0
high = 2**31-1

# # 1차시도 실패
# while low < high:
#     mid = (low+high)//2
#     cnt = 0
#     for thing in lan:
#         while thing >= mid:
#             thing -= mid
#             cnt += 1
    
#     if cnt >= n:
#         low = mid+1
#     else:
#         high = mid-1
# print((high+low)//2)

while low <= high:
    mid = (low+high)//2
    cnt = 0
    for thing in lan:
        cnt += thing//mid
    
    if cnt >= n:
        low = mid+1
    else:
        high = mid-1
print((high+low)//2)
