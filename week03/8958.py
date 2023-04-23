import sys

t = int(sys.stdin.readline())
for _ in range(t):
    case = list(sys.stdin.readline().rstrip())
    cnt = 0
    score = 0
    for i in range(len(case)):
        if case[i] == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)
