import sys
input = sys.stdin.readline

n = int(input())
values = list(map(int, input().split()))

# 1000이하의 자연수 중 소수들 판별하여 넣어놓기
numbers = [2, 3, 5, 7, 11, ]

# 리턴 변수
count = 0

for i in range(13, 1001, 2):
    flag = 0

    for j in range(len(numbers)):
        if i % numbers[j] == 0:
            flag = 1
            break

    if flag == 0:
        numbers.append(i)

for value in values:
    if value in numbers:
        count += 1

print(count)