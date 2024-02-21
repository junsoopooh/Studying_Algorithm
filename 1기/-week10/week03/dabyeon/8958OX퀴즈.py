import sys
input = sys.stdin.readline

T = int(input().rstrip())

result = []
for _ in range(T):
    str_line = input().rstrip()
    score = 0
    for e in str_line.split("X"):
        if e != '':
            score += int((1 + len(e)) / 2 * len(e))
            # print(f'len(e) : {len(e)}, score : {score}')
    result.append(score)
print(*result, sep='\n')