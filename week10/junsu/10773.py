import sys
k = int(sys.stdin.readline())
stk = []
for _ in range(k):
    num = int(sys.stdin.readline())
    if num != 0:
        stk.append(num)
    else:
        stk.pop()
print(sum(stk))