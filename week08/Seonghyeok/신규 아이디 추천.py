from collections import deque

alpha = 'abcdefghijklmnopqrstuvwxyz-_.0123456789'


def solution(new_id):
    new_id = list(new_id)
    removeList = []
    # 1단계 대문자 소문자로 치환
    for i in range(len(new_id)):

        if 65 <= ord(new_id[i]) <= 90:
            new_id[i] = chr(ord(new_id[i]) + 32)

        if new_id[i] not in alpha:
            removeList.append(new_id[i])

    # 2단계 특정 문자열 제외 모든 문자 제거
    if removeList:
        for i in removeList:
            new_id.remove(i)
    # 3단계 연속된 '.' 하나로 치환
    q = deque(new_id)
    dotRemoveList = []
    dotRemoveList.append(q.popleft())
    while q:
        val = q.popleft()
        dotRemoveList.append(val)
        if dotRemoveList[-1] == '.' and dotRemoveList[-1] == dotRemoveList[-2]:
            dotRemoveList.pop()
    # 4 단계
    dotq = deque(dotRemoveList)

    if len(dotq) >= 2:
        tmpleft = dotq.popleft()
        tmpright = dotq.pop()
        if tmpleft != '.':
            dotq.appendleft(tmpleft)
        if tmpright != '.':
            dotq.append(tmpright)

        dotRemoveList = list(dotq)
    elif len(dotq) == 1:
        tmp = dotq.pop()
        if tmp != '.':
            dotq.append(tmp)
        dotRemoveList = list(dotq)

    # 5 단계
    if len(dotRemoveList) == 0:
        dotRemoveList.append('a')

    resultList = []
    # 6 단계
    if len(dotRemoveList) >= 16:
        resultList = dotRemoveList[:15]
        if resultList[-1] == '.':
            del resultList[-1]
    if len(dotRemoveList) < 16:
        resultList = dotRemoveList

    # 7 단계
    if len(resultList) <= 2:
        while 1:
            resultList.append(resultList[-1])
            if len(resultList) == 3:
                break
    # List -> String
    answer = ''.join(resultList)

    return answer