def solution(lottos, win_nums):
    grade = 1
    result = []
    # 0의 개수
    zeroCnt = lottos.count(0)

    if zeroCnt == 6:
        return [1, 6]

    # 0 remove
    if zeroCnt > 0:
        while 0 in lottos:
            lottos.remove(0)

    for target in win_nums:
        if target in lottos:
            lottos.remove(target)

    # 최저 순위 확보
    grade += len(lottos)
    result.append(grade)

    # 모든 경우가 다 틀렸을때 예외처리
    if grade > 6:
        return [6, 6]
    # 최고 순위 확보
    grade += zeroCnt
    result.append(grade)

    return result