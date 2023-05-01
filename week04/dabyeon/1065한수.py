# 두자리 숫자는 무조건 한수.
# 그럼 100이상부터 한수인지 여부 구분하면 됨
# 1000은 한수가 아니니깐, 세자리 수의 경우, 0,1인덱스 값과 1,2 인덱스값만 비교하면 됨!!!

import sys
input = sys.stdin.readline

N = int(input().rstrip())

result = 0
if N < 100:
    result += N # 그냥 N을 print하게 하는게 좋을듯! for문을 계속 도니깐 비효율적!
else:
    result += 99
    for i in range(100, N+1):
        if (int(str(i)[0]) - int(str(i)[1])) == (int(str(i)[1]) - int(str(i)[2])):
            result += 1

print(result)