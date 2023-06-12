n = int(input())
stack = []
for _ in range(n):
    data = list(map(str, input().split()))
    print(data)
    if data[0] == 'push':
        stack.append(data[1])
    elif data[0] == 'pop':
        if stack.empty:
            print(-1)
        else:
            print(stack.pop())
    elif data[0] == 'size':
        print(len(stack))
    elif data[0] == 'empty':
        if stack.empty:
            print(1)
        else:
            print(0)
    elif data[0] == 'top':
        if stack.empty:
            print(-1)
        else:
            print(stack[-1])
