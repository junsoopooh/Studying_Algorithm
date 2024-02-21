def solution(s):
    pCnt = 0
    yCnt = 0
    for i in s:
        if i == 'p' or i == 'P':
            pCnt += 1
        elif i == 'y' or i == 'Y':
            yCnt += 1
    if pCnt == yCnt:
        return True
    else:
        return False
