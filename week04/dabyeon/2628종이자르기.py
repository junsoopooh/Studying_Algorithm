# 가로 0, 세로 1
# 가로 list, 세로 list, sort 후, 자르기!

import sys
input = sys.stdin.readline

length, width = map(int, input().rstrip().split())

T = int(input().rstrip())

length_list = [0, length]
width_list = [0, width]
for _ in range(T):
    flag, N = map(int, input().rstrip().split())

    if flag == 0:
        width_list.append(N)
    else:
        length_list.append(N)

length_list.sort()
width_list.sort()

def max_diff(list):
    max_diff = float("-inf")
    for i in range(1, len(list)):
        diff = abs(list[i] - list[i-1])
        if diff > max_diff:
            max_diff = diff

    return max_diff

print(max_diff(length_list) * max_diff(width_list))