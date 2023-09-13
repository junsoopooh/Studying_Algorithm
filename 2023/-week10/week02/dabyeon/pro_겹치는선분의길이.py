# https://school.programmers.co.kr/learn/courses/30/lessons/120876

lines = [[0, 1], [2, 5], [3, 9]]

def solution(lines):
    # 입력 범위 -100 ≤ a < b ≤ 100
    double = [0]*201 

    for x, y in lines:
        # print(f'x : {x}, y : {y}')
        for i in range(x,y):
            double[i] += 1

    return (201 - double.count(0) - double.count(1))

print(solution(lines))