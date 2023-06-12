import sys
input = sys.stdin.readline

# 테스트 케이스 수
n = int(input())

for _ in range(n):
    values = list(input().strip())

    stack = []

    # 성공/실패 플래그
    flag = True

    for value in values:
        if value == '(':
            # 만약 스택에 처음으로 들어가는 괄호라면,
            if len(stack) == 0:
                stack.append('(')

            # 스택의 마지막 값이 '(' 라면,
            elif stack[-1] == '(':
                stack.append('(')
            
            # 스택의 마지막 값이 ')' 라면,
            elif stack[-1] == ')':
                stack.pop()

        elif value == ')':
            # 만약 스택에 처음으로 들어가는 괄호라면,
            if len(stack) == 0:
                flag = False
                break

            # 스택의 마지막 값이 '(' 라면,
            elif stack[-1] == '(':
                stack.pop()
            
            # 스택의 마지막 값이 ')' 라면,
            elif stack[-1] == ')':
                flag = False
                break

    # 스택에 값이 남아있다면,
    if len(stack) != 0:
        flag = False

    if flag:
        print('YES')
    else:
        print('NO')
