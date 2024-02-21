def solution(s):
    # 닫힌 괄호가 가장 먼저 나오면 break 하고 return false
    # 스택이 비어 있는 경우 무조건 열린 괄호가 먼저 들어와야함
    stack = []
    answer = True
    for i in s:
        if not stack:
            if i == ")":
                return False
            stack.append(i)
        else:
            if i == ")":
                stack.pop()
            else:
                stack.append(i)
    if stack:
        answer = False
    return answer