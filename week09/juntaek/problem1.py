def solution(data, ext, val_ext, sort_by):
    answer = []
    dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    for d in data:
        value = d[dict[ext]]
        if value <= val_ext:
            answer.append(d)
    answer.sort(key = lambda x : x[dict[sort_by]])
    return answer