import sys
input = sys.stdin.readline

# 나무 수 n, 가져가려는 나무 길이 m
n, m = map(int, input().split())

# 나무 길이들
values = list(map(int, input().split()))

# 절단기 설정 높이의 최소, 최대값
minvalue = 0
maxvalue = max(values)

result = 0

while minvalue <= maxvalue:
    mid = (minvalue + maxvalue) // 2

    length = 0

    for value in values:
        if value - mid > 0:
            length += value - mid

    # "적어도" m미터 나무를 가져가야 함
    # 즉 넘쳐도 됨
    if length >= m:
        result = mid
        minvalue = mid + 1
    else:
        maxvalue = mid - 1

print(result)