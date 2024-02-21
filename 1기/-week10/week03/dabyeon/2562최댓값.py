import sys
input = sys.stdin.readline

N = 9
max_integer = float("-inf")
max_index = 0
for i in range(N):
    cur_num = int(input().rstrip())
    if max_integer < cur_num:
        max_integer = cur_num
        max_index = i + 1

print(max_integer)
print(max_index)