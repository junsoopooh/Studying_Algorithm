import sys
input = sys.stdin.readline

# 가로, 세로 길이
width, height = map(int, input().split())

# 가로, 세로 길이 리스트
width_list = [0, width, ]
height_list = [0, height, ]

# 가로, 세로 간격 리스트
width_interval = []
height_interval = []

# 잘라야 하는 점선의 수
n = int(input())

for _ in range(n):
    # 가로(0)/세로(1), 점선 번호
    a, b = map(int, input().split())

    if a == 0:
        height_list.append(b)
    else:
        width_list.append(b)

width_list.sort()
height_list.sort()

for i in range(len(width_list)-1):
    width_interval.append(width_list[i+1] - width_list[i])

for i in range(len(height_list)-1):
    height_interval.append(height_list[i+1] - height_list[i])

print(max(width_interval) * max(height_interval))