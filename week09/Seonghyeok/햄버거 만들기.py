def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            del s[-4:]
    return cnt


solution([2, 1, 1, 2, 3, 1, 2, 3, 1])