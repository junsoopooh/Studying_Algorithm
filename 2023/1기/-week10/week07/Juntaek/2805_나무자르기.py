import sys
input = sys.stdin.readline
n, m = map(int, input().split())
height_list = list(map(int, input().split()))
# print(height_list)

# height_list.sort()
# print(height_list)
left = 1
right = max(height_list)

while left <= right:
    height_sum = 0
    mid = (left + right) // 2
    for i in height_list:
        if i > mid:
            height_sum += (i-mid)
    # print(height_sum)
    if height_sum == m:
        print(mid)
        break
    elif height_sum < m:
        right = mid-1
    elif height_sum > m:
        left = mid+1