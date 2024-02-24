"""
짝지어 제거하기
https://school.programmers.co.kr/learn/courses/30/lessons/12973
"""
def solution(s):
    # 길이가 홀수면 뭔짓을 해도 하나 남음
    if len(s) % 2 == 1:
        return 0

    stack = []

    for c in s:
        # 스택이 있고 top이 현재 탐색중인 문자와 같으면 pop
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return 0 if stack else 1