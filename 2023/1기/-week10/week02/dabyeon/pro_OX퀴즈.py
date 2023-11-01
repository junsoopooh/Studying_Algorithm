# https://school.programmers.co.kr/learn/courses/30/lessons/120907

quiz = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]

def solution(quiz):
    answer = []
    for q in quiz:
        q_split = q.split("=")
        # print(q_split)
        if eval(q_split[0]) == int(q_split[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer