"""
압축
문제: https://school.programmers.co.kr/learn/courses/30/lessons/17684
"""
"""
1. 딕셔너리 생성하고 문자 길이 1이면 바로 리턴
2. 루프돌면서 새로운 키값 생성
3. 새로 생성한 문자의 맨 마지막을 제외한 문자열의 value를 정답에 넣어줌
4. 남은 문자가 있으므로 확인 후 넣어주던가 하면 됨
"""

def solution(msg):
    dic = dict(zip([chr(i) for i in range(65, 91)], [i for i in range(1, 27)]))

    if len(msg) == 1:
        return [dic[msg]]

    w = ""

    res, idx = [], 27

    for i in range(len(msg) - 1):
        w, c = w + msg[i], msg[i + 1]
        if w + c not in dic:
            dic[w + c] = idx
            idx += 1
            w = ""

    for i, j in dic.items():
        if j < 27:
            continue
        res.append(dic[i[:len(i) - 1]])

    tmp = w + c
    if not tmp:
        return res
    if tmp not in dic:
        dic[tmp] = idx
    res.append(dic[tmp[:len(tmp)]])
    return res