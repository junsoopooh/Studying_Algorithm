def solution(n):
    answer = 0
    lst = list(str(n))
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    tmp = sorted(lst, reverse=True)

    answer = int(''.join(map(str, tmp)))
    return answer
