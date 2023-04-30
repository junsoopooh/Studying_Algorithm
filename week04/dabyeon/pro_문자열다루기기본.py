s = "1234"

def solution(s):
    len_cnt = 0
    for cha in s:
        if '0' <= cha <= '9':
            len_cnt += 1

    flag = False
    if len(s) == len_cnt and (len(s) == 4 or len(s) == 6):
        flag = True

    return flag

print(solution(s))