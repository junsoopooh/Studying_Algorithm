import sys
input = sys.stdin.readline

def dp(n):
    # 1, 2, 3 수의 결과값은 각각 1, 2, 4
    if n in (1, 2):
        return n
    
    elif n == 3:
        return 4
    
    else:
        # 받은 수가 1, 2, 3이 될 때까지 dfs
        return dp(n-1) + dp(n-2) + dp(n-3)

# 테스트 케이스 수
t = int(input())

for _ in range(t):
    value = int(input())
    print(dp(value))

# 1일 때
# 1개

# 2일 때
# 1+1
# 2
# 2개

# 3일 때
# 1+1+1
# 1+2
# 2+1
# 3
# 4개

# 4일 때
# 1+1+1+1
# 2+1+1
# 1+2+1
# 1+1+2
# 2+2
# 3+1
# 1+3
# 7개

# 만약에 4를 넣었으면
# n-1 == 3 => 4
# n-2 == 2 => 2
# n-3 == 1 => 1

# 5일 때
# 1+1+1+1+1
# 2+1+1+1
# 1+2+1+1
# 1+1+2+1
# 1+1+1+2

# 2+2+1
# 2+1+2
# 1+2+2

# 2+3
# 3+2

# 10개