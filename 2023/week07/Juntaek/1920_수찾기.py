# import sys
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# search_list = list(map(int, input().split()))

# for i in search_list:
#     if i in a:
#         print(1)
#     else:
#         print(0)

### 이분 탐색 ###
n = int(input())
a = list(map(int, input().split()))
m = int(input())
search_list = list(map(int, input().split()))
a.sort()
print(a)

for i in range(len(search_list)):
    left = 0
    right = len(a)-1
    while left <= right:
        mid = (left + right)//2
        if search_list[i] == a[mid]:
            print(1)
            break
        elif search_list[i] < a[mid]:
            right = mid - 1
        elif search_list[i] > a[mid]:
            left = mid + 1
    else:
        print(0)
