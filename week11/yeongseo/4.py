def is_right(p): # 올바른 괄호 문자열 인지 확인
    stack = []
    for i in p:
        if i == "(":
            stack.append("(")
        else: 
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    
    if len(stack) == 0:
        return True 
    else:
        return False
    
def divide(s): # 2번 수행
    left, right = 0, 0 
    for i in range(len(s)):
        if s[i] == "(":
            left += 1
        else:
            right += 1 
        if left == right:
            return s[:i+1], s[i+1:]

def solution(p):
    if len(p) == 0:
        return ""
    
    u, v = divide(p)
    
    if is_right(u):
        return u + solution(v)
    else:
        ans = "("
        ans += solution(v)
        ans += ")"
        for i in u[1:len(u) - 1]:
            if i == "(":
                ans += ")"
            else:
                ans += "("
        return ans

   