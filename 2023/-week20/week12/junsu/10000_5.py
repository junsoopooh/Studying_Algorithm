import sys

n = int(sys.stdin.readline())
circles =[]
stk=[]
ans = n+1 # 원이 생기면 원 내부 라는 새로운 영역이 생김. 가장 처음에는 밖도 생기니 +1

for i in range(n):
    x,r = map(int, sys.stdin.readline().split())
    circles.append([x-r, x+r]) # 원의 왼쪽 끝, 오른쪽 끝 저장
circles.sort(key = lambda x: (x[0], -x[1])) # 왼쪽 끝을 기준으로 오름차순 정렬, 같을땐 오른쪽 끝을 내림차순 정렬

start = circles[0][0] # 가장 왼쪽에 있는 원의 왼쪽
end = circles[0][1] # 가장 왼쪾에 있는 원의 오른쪽

for i in range(1,n): # 가장 왼쪽 원 제외하고 반복문
    x1 = circles[i][0] # 주목하는 원의 왼쪽 
    x2 = circles[i][1] # 주목하는 원의 오른쪽 
    if start == x1: # 이전 원과 왼쪽이 동일하다면?
        stk.append([x2,end]) # x1부터 x2까지는 현재 주목하는 원이 차지했으니 x2부터 end까지만 원이 차면 내부를 반으로 나눈다.
        end = x2 # 새롭게 끝을 이전원의 오른쪽으로 설정
    else: # 이전 원과 왼쪽 끝이 동일하지않다.
        start = x1 # 새롭게 시작점을 현재 주목하는 원의 왼쪽끝으로 설정
        while len(stk)>0: # 스택에 원소가 있다는건 아직 내부가 반으로 나뉘어지는지 검사해야할 원이 남았다는 뜻.
            if start == stk[-1][0]: # 방금 스택에 들어간 원소의 0번 인덱스는 어디까지 원이 이어져있었는지를 말한다. 거기서부터 새로운 원이 시작된다면?
                end = x2 #새로운 원의 오른쪽을 끝점으로 설정
                if stk[-1][1] == x2: #1번 인덱스는 검사하는 원의 오른쪽이다. 새로운원이 거기에 닿았다면?
                    ans += 1 # 내부가 반으로 나뉘어졌으니 영역을 +1 한다.
                    stk.pop() # 검사가 끝났으니 stk 제거
                    break
                else: # 아직 닿지 못했다면?
                    stk[-1][0] = end # 원이 끊어지지 않고 이어져있었던 곳을 현재 원의 오른쪽으로 수정한다.
                    break
            elif start > stk[-1][0]: # 더이상 원이 이어지지 않았다. 현재 검사하는원은 내부가 반으로 나뉘지 않음.
                end = stk.pop() # 검사할 필요 없으니 제거
            else:
                break
        end = x2 # 끝을 현재 원의 오른쪽으로 재설정.

print(ans)