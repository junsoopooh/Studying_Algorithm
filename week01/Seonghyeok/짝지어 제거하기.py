from collections import deque

def solution(s):
    s = deque(s)
    tmp = deque()
    idx = 0
    while s:
        target = s.popleft()
        if len(s) > 0 and target == s[0]:
            s.popleft()
        else:
            if len(tmp) > 0 and target == tmp[-1]:
                tmp.pop()
            else:
                tmp.append(target)

    if len(tmp) > 0:
        return 0
    else:
        return 1
