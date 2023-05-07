# 2^N / 2 진입 기준
# 1 ~ 4 분면 중 어디에 속하는지 판단

# 1사분면 (0,0) 
# 2사분면 (0, 2^N / 2) 
# 3사분면 (2^N / 2, 0) 
# 4사분면 (2^N / 2, 2^N / 2)

# 진입 후, 기준점 (0,0)으로 초기화
import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

flag = 2**(N) // 2

result = 0
while flag > 0:
    # 1 사분면
    if r < flag and c < flag:
        flag //= 2
    # 2 사분면
    elif r < flag and c >= flag:
        result += (flag)*(flag)
        c -= flag # 기준점 다시 (0,0)으로
        flag //= 2
    # 3 사분면
    elif r >= flag and c< flag: 
        result += 2*(flag)*(flag)
        r -= flag # 기준점 다시 (0,0)으로
        flag //= 2
    # 4 사분면
    elif r>= flag and c >= flag:
        result += 3*(flag)*(flag)
        r -= flag # 기준점 다시 (0,0)으로
        c -= flag # 기준점 다시 (0,0)으로
        flag //= 2

print(result)