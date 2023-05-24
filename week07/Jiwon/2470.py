import sys
input = sys.stdin.readline

# 전체 용액 수
n = int(input())

# 용액 특성 리스트
values = list(map(int, input().split()))
values.sort()

# 합이 0과 가까운 두 수 구하기

minvalue = sys.maxsize
result = []

left = 0
right = n-1

while left <= right:
    sumvalue = values[left] + values[right]

    if abs(sumvalue) < minvalue:
        minvalue = abs(sumvalue)
        result = [values[left], values[right]]

    # 만약 합이 음수라면 left + 1
    if sumvalue < 0:
        left += 1
    elif sumvalue > 0:
        right -= 1
    else:
        break

print(result[0], result[1])