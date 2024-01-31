def isSquare(n, sq):
    for i in range(1, sq):
        if i * i == n:
            return i
    return -1


def solution(n):
    answer = 0
    if n == 1:
        return 4

    if n > 10:
        sq = n // 2
    else:
        sq = n

    answer = isSquare(n, sq)

    if answer == -1:
        return -1
    else:
        return (answer + 1) * (answer + 1)