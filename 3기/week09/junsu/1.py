# [데이터 분석](https://school.programmers.co.kr/learn/courses/30/lessons/250121)

def solution(data, ext, val_ext, sort_by):
    answer = []
    for x in data:
        arr = dict()
        arr["code"] = x[0]
        arr["date"] = x[1]
        arr["maximum"] = x[2]
        arr["remain"] = x[3]
        if arr[ext] < val_ext:
            answer.append(x)
    if sort_by == 'code':
        idx = 0
    elif sort_by == 'date':
        idx = 1
    elif sort_by == 'maximum':
        idx = 2
    else:
        idx = 3
    answer.sort(key = lambda x: (x[idx]))
    return answer