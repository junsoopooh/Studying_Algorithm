def solution(s):
    stack = []
    
    for ch in s:
        if len(stack) != 0 and stack[-1] == ch:
            stack.pop()
        
        else:
            stack.append(ch)
    
    return 1 if len(stack) == 0 else 0