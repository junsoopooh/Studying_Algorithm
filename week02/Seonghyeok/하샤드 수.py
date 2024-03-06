def solution(x):
    tmp = 0
    for i in str(x):
        tmp += int(i)
    if (x % tmp) == 0:
        return True
    else:
        return False