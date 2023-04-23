import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n_score = list(map(int, input().rstrip().split()))

    avg = sum(n_score[1:]) / n_score[0]
    cnt = 0
    for score in n_score[1:]:
        if score > avg:
            cnt += 1

    print('{:.3f}%'.format(round(cnt/n_score[0]*100, 3)))