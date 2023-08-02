import sys
input = sys.stdin.readline

# 명령 개수
n = int(input())

stack = []

for _ in range(n):
    command = input().strip()

    if 'push' in command:
        stack.append(command.split(' ')[1])
    
    elif command == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif command == 'size':
        print(len(stack))

    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif command == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])