import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 9)

# 문제 1: N단계의 XYZ 문자열의 길이를 구한다.
# 문제 2: N단계의 XYZ 문자열에서 k번째 문자가 무엇인지 구한다.
# 문제 3: N단계의 XYZ 문자열에서 특정한 문자가 몇 번 나타나는지 구한다.

values = ['X', 'YZ', 'ZX', ]

# 문제 번호
problem = int(input())

# 자연수 N, 단계를 나타냄
n = int(input())

# 문제가 2번이면 자연수 k
if problem == 2:
    k = int(input())

# 문제가 3번이면 X 또는 Y 또는 Z
if problem == 3:
    target = input().strip()

for i in range(3, n):
    values.append(values[i-3] + values[i-2])

if problem == 1:
    print(len(values[-1]))
elif problem == 2:
    print(values[-1][k-1])
else:
    print(values[-1].count(target))