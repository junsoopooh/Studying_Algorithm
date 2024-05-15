"""
조이스틱
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42860
"""

def solution(name):
    n = len(name)
    print(n)
    # 알파벳 변경 최소값
    up_down = sum([min(ord(char) - ord("A"), ord("Z") - ord(char) + 1) for char in name])

    # A가 없으면 그냥 커서 이동횟수 n-1 번 더해서 리턴
    if "A" not in name:
        return up_down + (n - 1)

    # 만약 A가 많은 부분이 있다면 그 부분은 탐색안하는게 최소 횟수임
    left_right = 1e9

    for i in range(n):
        idx = i + 1

        while idx < n and name[idx] == "A":
            idx += 1
        print(idx)
        left_right = min(left_right, i * 2 + n - idx, 2 * (n - idx) + i)

    return left_right + up_down