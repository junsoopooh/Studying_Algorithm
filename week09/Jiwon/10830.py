import sys
input = sys.stdin.readline

# 행렬의 크기 n과 거듭제곱할 값 b
n, b = map(int, input().split())

# 행렬 리스트
values = [list(map(int, input().split())) for _ in range(n)]

# 행렬의 곱을 계산하는 함수
def getMultiple (arr1, arr2):
    temp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                # 여기서 1000을 나눠주지 않으면 시간초과
                temp[i][j] += arr1[i][k] * arr2[k][j] % 1000

    return temp

# 지수를 나눠 계산하는 함수 (백준 제곱 1629 문제와 동일)
def getValue (values, b):
    # 지수가 1이면,
    if b == 1:
        return values
    else:
        temp = getValue(values, b//2)

        # 지수가 짝수면,
        if b % 2 == 0:
            return getMultiple(temp, temp)
        # 지수가 홀수면,
        else:
            return getMultiple(getMultiple(temp, temp), values)
        
results = getValue(values, b)

for result in results:
    for value in result:
        # 마지막 출력 해줄 때 나누는 게 베스트일 듯
        print(value % 1000, end=" ")
    print()