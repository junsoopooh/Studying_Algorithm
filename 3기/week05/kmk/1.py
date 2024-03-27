"""
대충 만든 자판
https://school.programmers.co.kr/learn/courses/30/lessons/160586
"""
def solution(keymap, targets):
    res = []

    dic = dict()

    for s in keymap:
        for i in range(len(s)):
            dic[s[i]] = i + 1 if s[i] not in dic else min(dic[s[i]], i + 1)

    for s in targets:
        cnt = 0
        for c in s:
            if c in dic:
                cnt += dic[c]
            else:
                cnt = 0
                break
        cnt = cnt if cnt > 0 else -1
        res.append(cnt)

    return res