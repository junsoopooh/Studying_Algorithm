import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    arr.append([x-r, x+r])  # 왼쪽점과 오른쪽 점을 원소로 하는 배열 삽입
# 왼쪽 점이 가장 작은 순서로, 같은 원들은 오른쪽 점이 가장 큰 순서로 정렬
arr.sort(key=lambda x: (x[0], -x[1]))
cnt = 1 
stk = []
if n != 1:
    for i in range(n):
        if not stk:
            stk.append(arr[i])
            right = stk[0][0]
        for j in range(i+1, n):
            if arr[j][0] != right:
                break
            else:
                if arr[j][1] == stk[0][1]:
                    cnt += 1
                    break
                else:
                    right = arr[j][1]
    stk.pop()

print(cnt+n)
