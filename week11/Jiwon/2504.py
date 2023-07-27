import sys
input = sys.stdin.readline

values = list(input().strip())

# 여기에는 '('와 '['만 들어감
stack = []

total = 0
temp = 1

for i in range(len(values)):
    if values[i] == '(':
        temp *= 2
        stack.append('(')

    elif values[i] == '[':
        temp *= 3
        stack.append('[')

    elif values[i] == ')':
        # 값이 있어야 pop할 수 있음
        if not stack:
            total = 0
            break

        # 닫을 때는 같은 기호여야 함
        if stack[-1] == '(':
            # 처음 닫을 때만 더해줌
            if values[i-1] == '(':
                total += temp
            stack.pop()
            temp //= 2
        else:
            total = 0
            break

    else:
        # 값이 있어야 pop할 수 있음
        if not stack:
            total = 0
            break

        # 닫을 때는 같은 기호여야 함
        if stack[-1] == '[':
            # 처음 닫을 때만 더해줌
            if values[i-1] == '[':
                total += temp
            stack.pop()
            temp //= 3
        else:
            total = 0
            break

if stack:
    total = 0

print(total)