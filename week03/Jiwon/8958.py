import sys
input = sys.stdin.readline

# 테스트 케이스 수
n = int(input())

for _ in range(n):
    values = list(input().strip())
    scores = []

    for i in range(len(values)):
        if i == 0:
            if values[i] == 'O':
                scores.append(1)
            else:
                scores.append(0)
        else:
            if values[i] == 'O':
                scores.append(scores[i-1] + 1)
            else:
                scores.append(0)

    print(sum(scores))