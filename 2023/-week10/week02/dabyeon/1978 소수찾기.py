import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().rsplit()))

n = max(nums)

prim = [1] + [0]*n
prim[1] = 1 # 1 소수에서 제외
prim[2] = 1 # 2 소수에서 제외

for i in range(2, int((n+1)**0.5)+1):
    for j in range(i*i, n+1, i):
        # print(f'i : {i}, j : {j}')
        if prim[j] != 0:
            continue
        else:
            prim[j] = 1

# print(prim)

cnt = 0
for num in nums:
    if prim[num] == 0:
        cnt += 1
print(cnt)