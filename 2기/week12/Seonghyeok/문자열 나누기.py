def solution(s):
    answer = 0
    exitFlag = False
    while 1:
        if len(s) == 0 or len(s) == 1 or exitFlag == True:
            break
        firstCnt = 0
        remainCnt = 0
        Firstchr = s[0]

        for i in range(len(s)):
            if i == len(s) - 1:
                exitFlag = True
            if Firstchr == s[i]:
                firstCnt += 1
            else:
                remainCnt += 1

            if firstCnt == remainCnt:
                answer += 1
                s = s[i + 1:]
                break
    if len(s) >= 1:
        answer += 1
    return answer