import sys
input = sys.stdin.readline

# 테스트 케이스 수
c = int(input())

for _ in range(c):
    values = list(map(int, input().split()))

    # 학생 수
    c = values[0]

    # 학생들 점수
    values.pop(0)

    # 평균
    avg = sum(values) / c

    # 평균을 넘는 학생 수
    count = 0
    for value in values:
        if value > avg:
            count += 1

    # 평균을 넘는 학생 비율
    print(f'{count/c:.3%}')