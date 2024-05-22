"""
카펫
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42842
"""

def solution(brown, yellow):
    # 갈색에서 양 모서리 4개 빼줌
    start = brown - 4

    # 가로 개수 = 세로 개수를 2개로 잡으면 start - 2가 가로의 최대 개수임.
    r, c = start - 2, 2

    # 가로 길이 = 가로 개수 // 2, 세로 길이 = 세로 개수 // 2
    # 넓이가 yellow가 되면 처음에 빼줬던 양 모서리 4개 더 해주고 끝
    while 1:
        a, b = int(r // 2), int(c // 2)
        if a * b == yellow:
            r, c = a + 2, b + 2
            break
        else:
            r -= 2
            c += 2

    return [r, c]