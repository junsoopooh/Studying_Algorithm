import sys
input = sys.stdin.readline

n = int(input())

def solve(num):
    # 한수 카운팅
    count = 99

    for i in range(100, num+1):
        # 각 자리를 비교하기 위해, 값은 무조건 세자리 수
        number = list(map(int, str(i)))

        if number[0] - number[1] == number[1] - number[2]:
            count += 1

    print(count)

# 100보다 작으면 모두 한수
if n < 100:
    print(n)
else:
    # 100보다 큰 값이 입력되었을 때만 넘어감
    solve(n)