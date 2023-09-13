import sys
input = sys.stdin.readline
n = int(input())
circles = []
stack = []
answer = 1

# x좌표랑 반지름을 하나로 묶어서 일단 리스트에 원의 개수만큼 for문 돌려서 다 담기
for _ in range(n):
  x, r = map(int, input().split())
  # 원 하나당 괄호가 2개. 여는 괄호의 x좌표는 x-r, 닫는 괄호는 x+r
  circles.append((x-r, '('))
  circles.append((x+r, ')'))
  
# x좌표 기준으로 오름차순 정렬 진행. 만약 x좌표가 같으면 ')'가 먼저오게 정렬
# ord는 문자의 아스키 코드 반환 이때 ')'가 더 숫자가 높으니 -붙여야지 ')'가 앞으로 오게됨
circles.sort(key = lambda x: (x[0], -ord(x[1])))

for i in range(n*2):
  position, bracket = circles[i]
  
  # 스택에 아무것도 없는 상황이다? 앞에서 정렬 했으니 그냥 넣어
  if len(stack) == 0:
    # 상태 0은 겹치지 않아서 원이 하나인 경우
    # 상태 1은 좌표가 겹쳐서 원이 2개인 경우
    stack.append({'pos': position, 'bracket': bracket, 'state': 0})
    continue
  
  # 스택 탑이 여는 괄호다? x좌표 위치가 현재 좌표랑 같으면 겹치는거니까 스택 탑 상태를 1로 변경 
  if bracket == '(':
    if stack[-1]['pos'] == position:
      stack[-1]['state'] = 1
    stack.append({'pos': position, 'bracket': bracket, 'state': 0})
  
  # 닫힌 괄호가 들어올 때
  else:
    # 스택 탑의 상태가 0이면 + 1
    if stack[-1]['state'] == 0:
      answer += 1
    
    # 스택 탑의 상태가 1이면 + 2
    elif stack[-1]['state'] ==1:
      answer += 2
    stack.pop()
    
    # 원이 겹치지 않는 경우는 스택 탑의 상태를 0으로 변경
    if i != n*2-1:
      if circles[i+1][0] != position:
        stack[-1]['state'] = 0
print(answer)