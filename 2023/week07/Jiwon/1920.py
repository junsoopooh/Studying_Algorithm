import sys
input = sys.stdin.readline

# 보기 리스트 개수 n
n = int(input())

# 보기 리스트
values = list(map(int, input().split()))
values.sort()

# 테스트 케이스 m
m = int(input())

# 케이스 리스트
cases = list(map(int, input().split()))

def binary_search(target):
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2

        if values[mid] == target:
            return 1
        elif values[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return 0

for case in cases:
    print(binary_search(case))

# 시간 초과
# for case in cases:
#     if case in values:
#         print(1)
#     else:
#         print(0)