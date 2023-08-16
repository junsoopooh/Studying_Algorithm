import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
plus, minus, multiple, division = map(int, sys.stdin.readline().split())

arr = []


def dfs(tmp, cnt, a, b, c, d):
    if cnt == n:
        arr.append(tmp)
        return

    if a:
        tmp += nums[cnt]
        a -= 1
        cnt += 1
        dfs(tmp, cnt, a, b, c, d)
        cnt -= 1
        a += 1
        tmp -= nums[cnt]

    if b:
        tmp -= nums[cnt]
        b -= 1
        cnt += 1
        dfs(tmp, cnt, a, b, c, d)
        cnt -= 1
        b += 1
        tmp += nums[cnt]

    if c:
        tmp *= nums[cnt]
        c -= 1
        cnt += 1
        dfs(tmp, cnt, a, b, c, d)
        cnt -= 1
        c += 1
        tmp = tmp // nums[cnt]

    if d:
        if tmp >= 0:
            tmp = tmp//nums[cnt]
        else:
            r_tmp = abs(tmp)//nums[cnt]
            tmp = -1 * r_tmp
        d -= 1
        cnt += 1
        dfs(tmp, cnt, a, b, c, d)
        cnt -= 1
        d += 1
        if tmp >= 0:
            tmp = abs(tmp)*nums[cnt]
        else:
            r_tmp = abs(tmp)*nums[cnt]
            tmp = -1 * r_tmp


dfs(nums[0], 1, plus, minus, multiple, division)
print(max(arr))
print(min(arr))
