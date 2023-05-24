import itertools

n, s = map(int, input().split())
a = list(map(int, input().split()))
# print(a)
cnt = 0

for i in range(1, n+1):
    combi = itertools.combinations(a, i)
    for j in combi:
        if sum(j) == s:
            cnt += 1
print(cnt)