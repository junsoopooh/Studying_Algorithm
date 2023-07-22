import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    x,r = map(int,sys.stdin.readline().split())
    arr.append([x-r,x+r]) # 왼쪽점과 오른쪽 점을 원소로 하는 배열 삽입
arr.sort(key = lambda x: (x[0], -x[1])) # 왼쪽 점이 가장 작은 순서로, 같은 원들은 오른쪽 점이 가장 큰 순서로 정렬
cnt = 1 # 원이 그려지면 무조건 가장 밖은 생기므로 1부터 시작
right = arr[0][1] # 가장 첫번째 원의 오른쪽 끝점 설정
stk = [] # 현재 가장 밖으로 설정한 원을 저장해둔다.

full = False # 내부가 절반으로 나뉘어졌는지 표시하는 flag
for dot in arr:
    if not stk: # 처음 원이므로 가장 큼. 시작점, 끝점을 설정
        stk.append(dot)
        tmp = stk[0][0] # 시작점
        right = stk[0][1] # 끝점
        max_val = stk[0][0] # 현재 원 내부의 왼쪽부터 안 끊기고 최대로 이어진 지점. 맨처음엔 왼쪽에서 시작
        cnt += 1 # 원이 그러졌으니 나뉘어짐
        continue
    if dot[0] == tmp: # 시작점이 같은 원. 내접한다는 뜻
        cnt += 1
        if dot[1] != right: # 시작점이 같은 원 중 가장 큰 원의 끝점이 아직 닿지 않아서 절반으로 나누지 못했음.
            max_val = dot[1] # 시작점부터 여기까지는 끊기지 않고 이어졌다. 아직 큰원의 내부가 반으로 나눠질 가능성 존재
    else: # 시작점이 기존과 달라졌다.
        if dot[0] >= right: # 기존에 가장 큰 원 밖으로 새롭게 시작되었음. 재설정
            stk.pop()
            stk.append(dot)
            tmp = stk[0][0]
            right = stk[0][1]
            max_val = stk[0][0]
            cnt += 1
            continue
        else: # 아직 기존 원 내부에 있음. 
            if dot[0] > max_val: # 아직 내부지만 기록해둔 끝점과 시작점이 달라짐. 내부가 절반으로 나눠질 가능성 사라짐.
                cnt += 1
            elif dot[0] == max_val: # 끝점에서 다시 시작점이 시작되었음. 여전히 가능성은 존재.
                max_val = dot[1]
                cnt += 1
                if dot[1] == right: # 끝 점이 가장 큰 원의 끝점에 닿았음. 내부는 반으로 갈라졌음. 나눠진 공간을 +1 해야함.
                    cnt += 1
                    full = True
                else: # 아직 닿진 않았으나 더 확인해봐야함
                    max_val = dot[1]
print(cnt)