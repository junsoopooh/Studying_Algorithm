import sys
input = sys.stdin.readline

target = input().strip()
bomb = input().strip()

target_len = len(target)
bomb_len = len(bomb)

stack = []

for i in range(target_len):
    stack.append(target[i])

    if ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")