# 하노이의 탑
def solution(n):
    answer = []

    def move(a, b, x):
        if x == 1:
            answer.append([a, b])
        else:
            move(a, 6-a-b, x-1)
            move(a, b, 1)
            move(6-a-b, b, x-1)

    move(1, 3, n)
    return answer
