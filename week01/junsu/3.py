def solution(s):
    arr = list(s)
    stk = []
    for i in range(len(s)):
        if not stk:
            stk.append(arr[i])
            continue
        else:
            if stk[-1] == arr[i]:
                stk.pop()
            else:
                stk.append(arr[i])
    if not stk:
        answer = 1
    else:
        answer = 0
    return answer
