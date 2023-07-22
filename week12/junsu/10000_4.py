import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    arr.append([x-r, x+r])
arr.sort(key=lambda x: (x[0], -x[1]))
stk = []
cnt = 1

for dot in arr: # 원 하나씩 본다.
    cnt += 1 # 원이 있으면 원 내부 라는 영역이 무조건 생성되므로 +1
    if not stk: # 맨 처음 차례라면 일단 넣는다.
        stk.append(dot)
        continue
    left = stk[-1][0] # 현재 가장 가까운 밖의 원의 왼쪽 끝과 오른쪽 끝 설정
    right = stk[-1][1]
    if dot[0] == left: # 현재 가장 가까운 밖의 원과 왼쪽 끝이 동일할 때
        stk.append(dot) # 이 원을 새로운 가장 가까운 밖의 원으로 설정
    elif dot[0] > left: # 가장 가까운 밖의 원과 왼쪽 끝이 다를 때
        stk.pop() # 기존의 가까운 밖의 원은 내부를 나눌 수 없게 됐으니 제거
        if dot[0] < right: # 하지만 여전히 가장 가까운 밖의 원의 내부에 있을 때
            stk.append(dot) # 현재의 원을 새로운 가장 가까운 밖의 원으로 설정
        elif dot[0] == right: # 이번 원이 가장 가까운 밖의 원의 끝에서부터 시작되는 원이라면?
            if not stk: # 현재 어떤 원의 내부가 아니라면?
                stk.append(dot) # 가장 가까운 원으로 설정
            elif dot[1] != stk[-1][1]: # 원의 내부지만 오른쪽 끝이 닿지 않았다면?
                stk.append(dot) # 그 원을 가장 가까운 밖의 원으로 설정
            elif dot[1] == stk[-1][1]: # 가장 가까운 밖의 원의 오른쪽 끝에 닿았다.
                cnt += 1 # 위아래로 영역이 나눠졌으므로 1 추가
                stk.pop() # 만족한 원은 제거 
                stk.append(dot) # 검사를 위한 원 설정             
        else: # 기존 밖의 원의 외부이면서 접하지 않는다면?
            stk.append(dot) # 새로운 목표 설정

print(cnt)
반례 : https://velog.io/@cherrym/baekjoon-10000-areas-made-of-circle