"""
오픈 채팅방
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42888
"""

"""
딕셔너리에 유저 아이디 기록 후 해결
"""
from collections import Counter

def solution(record):
    answer = []
    dic = Counter()

    enter = "님이 들어왔습니다."
    leave = "님이 나갔습니다."

    for r in record:
        r = r.split()
        if r[0] != "Leave":
            dic[r[1]] = r[2]

    for r in record:
        r = r.split()

        if r[0] != "Change":
            answer.append(dic[r[1]] + leave if r[0] == "Leave" else dic[r[1]] + enter)

    return answer