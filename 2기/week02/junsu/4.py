# 올바른 괄호 

from collections import deque
def solution(s):
    answer = True
    arr = list(s)
    q = deque()
    for i in range(len(s)):
        if arr[i] == '(':
            q.append(arr[i])
        else:
            if not q or q[-1] != '(':
                return False
            elif q[-1] == '(':
                q.pop()
                continue
    if q:
        return False
    else:
        return answer
