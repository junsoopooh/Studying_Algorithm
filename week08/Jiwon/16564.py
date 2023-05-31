import sys
input = sys.stdin.readline

# 캐릭터 개수 n, 올릴 수 있는 레벨 총합 k
n, k = map(int, input().split())

# 현재 각 캐릭터의 레벨
levels = [int(input()) for _ in range(n)]

# 이번에는 가능한 "최대 목표레벨"이 기준이겠네
minlevel = min(levels)
maxlevel = max(levels) + k

result = 0

while minlevel <= maxlevel:
    mid = (minlevel + maxlevel) // 2

    # 해당 레벨로 올리는데 필요한 레벨 확인
    need = 0
    for level in levels:
        if level < mid:
            need += mid - level
    
    if need > k:
        maxlevel = mid - 1
    else:
        result = mid
        minlevel = mid + 1

print(result)