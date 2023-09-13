import sys

n = int(sys.stdin.readline())
arr = [0]
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

dp = [0 for _ in range(n+1)]
dp[1] = 0


def cal(p, q):
    return p[0]*p[1]*q[1]


def mix(p, q):
    return [p[0], q[1]]


idx = 2
while idx <= n:
    if idx == 2:
        dp[idx] = cal(arr[idx-1], arr[idx])
        idx += 1
        continue

    tmp = []
    for i in range(1, idx):
        cnt = 0
        cnt += dp[i]
        k = arr[i+1]
        j = i+2
        cnt += arr[1][0]*k[0]*arr[idx][1]
        while j <= idx:
            cnt += cal(k, arr[j])
            k = mix(k, arr[j])
            j += 1
        tmp.append(cnt)
    dp[idx] = min(tmp)
    idx += 1
print(dp[-1])
