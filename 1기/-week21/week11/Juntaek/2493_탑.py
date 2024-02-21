import sys
input = sys.stdin.readline
n = int(input())
tops = list(map(int, input().split()))
stack = []
answer = [0] * n
for i in range(len(tops)):
	while stack:
		if stack[-1][1] < tops[i]:
			stack.pop()
		else:
			answer[i] = stack[-1][0] + 1
			break
	stack.append((i, tops[i]))
print(*answer)