# 숫자 짝꿍
def solution(X, Y):
    x = str(X)
    nx = len(x)
    y = str(Y)
    ny = len(y)
    arr = [0 for _ in range(10)]
    arr_x = [0 for _ in range(10)]
    arr_y = [0 for _ in range(10)]
    ans = []
    flag = 0

    for i in range(nx):
        tmp = x[i]
        arr_x[int(tmp)] += 1
    for j in range(ny):
        tmp = y[j]
        arr_y[int(tmp)] += 1

    for k in range(10):
        arr[k] = min(arr_x[k], arr_y[k])

    for i in range(9, -1, -1):
        if arr[i]:
            flag = max(flag, i)
        cnt = arr[i]
        while cnt > 0:
            ans.append(i)
            cnt -= 1

    if flag:
        answer = ''.join(str(i) for i in ans)
    else:
        if arr[0]:
            answer = "0"
        else:
            answer = "-1"
    return answer
