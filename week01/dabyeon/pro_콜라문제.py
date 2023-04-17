a = 3
b = 2
n = 10

# cnt = 0
# while(n >= 2):
#     if n-a < 0:
#         break
#     n = n - a + b
#     cnt += 1*b

# print(cnt)

# 계속 값이 변하는 n와 cnt를 파라미터 값으로 가짐.
def recursion(a, b, n, cnt=0):
    # 남은 병의 갯수가 두개 미만이면, 콜라 교환이 불가능하다.
    if n < 2:
        return cnt
    elif n - a < 0:
        return cnt
    else:
        n = n - a + b
        cnt += b
        return recursion(a, b, n, cnt)

print(recursion(a, b, n))