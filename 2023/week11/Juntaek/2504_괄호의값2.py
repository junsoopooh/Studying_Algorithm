# (x) 곱하기 2
# [x] 곱하기 3
# ()[] 더하기 
# 일단 여는 소괄호 들어오면 곱하기 2, 여는 대괄호 들어오면 곱하기 3
# ([]) [()] ()[] []()
# 덧셈 계산에 필요한 변수가 필요할듯?
# 언제 덧셈을 해야할까? () [] 이때는 그냥 pop해버리나? ([](([[]])))
# 닫는 괄호가 나온 이후에 여는 괄호가 나오면 덧셈 같은데.?
#괄호의값
bracket = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break

        if bracket[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break

        if bracket[i-1] == "[":
            answer += tmp
        
        stack.pop()
        tmp //= 3
if stack:
    print(0)
else:
    print(answer)