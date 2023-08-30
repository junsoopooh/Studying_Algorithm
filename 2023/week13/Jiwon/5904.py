import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

n = int(input())

# 찾으려는 위치, 길이, 차수
def moo(x, length, degree):
    if x <= 3:
        return "moo"[x-1]
    
    # 전체 길이 = 이전 문자열 X 2 + 현재 차수 + 3
    total_len = length * 2 + degree + 3

    # 찾으려는 위치가 왼쪽 수열에 포함된다면
    if total_len < x :
        return moo(x, total_len, degree + 1)
    else:
        # 찾으려는 위치가 가운데에 포함된다면
        if length < x <= length + (degree + 3):
            if x == length + 1:
                return 'm'
            else:
                return 'o'
        # 찾으려는 위치가 오른쪽 수열에 포함된다면
        else:
            x -= length + (degree + 3)
            return moo(x, 3, 1)

print(moo(n, 3, 1))