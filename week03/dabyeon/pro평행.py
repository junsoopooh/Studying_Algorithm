dots = [[3, 5], [4, 1], [2, 4], [5, 10]]

def gradient(a, b):
    return (a[1] - b[1])/(a[0] - b[0])

# 0, 1 / 2, 3
# 0, 2 / 1, 3
# 0, 3 / 1, 2

def solution(dots):
    answer = 0
    if gradient(dots[0], dots[1]) == gradient(dots[2], dots[3]):
        return 1
    elif gradient(dots[0], dots[2]) == gradient(dots[1], dots[3]):
        return 1
    elif gradient(dots[0], dots[3]) == gradient(dots[1], dots[2]):
        return 1
    return 0

print(solution(dots))