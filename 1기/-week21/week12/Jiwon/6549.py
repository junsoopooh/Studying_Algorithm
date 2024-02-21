import sys
input = sys.stdin.readline

while True:
    values = list(map(int, input().split()))
    
    # 0일 때 종료
    count = values[0]
    if count == 0:
        break
    else:
        values.pop(0)

    total_sum = 0
    stack = []

    for i in range(count):
        width = i

        # 왼쪽 > 오른쪽 일 때
        while stack and stack[-1][0] >= values[i]:
            height, width = stack.pop()
            total_sum = max(total_sum, height * (i-width))

        # 높이, 넓이
        stack.append([values[i], width])

    for h, w in stack:
        total_sum = max(total_sum, h * (count-w))

    print(total_sum)