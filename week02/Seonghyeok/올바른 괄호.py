from collections import deque

def solution(s):
    answer = []
    dq = deque(s)
    # 첫번째 큐 값은 차피 넣어야하니까
    answer.append(dq.popleft())
    while dq:
        val = dq.popleft()
        # answer 리스트가 비어있을경우
        if not answer:
            answer.append(val)
        else:
            # answer의 마지막 괄호가 열려있을때
            if answer[-1] == '(':
                # 괄호가 닫힐수있는경우
                if val == ')':
                    answer.pop()
                # 괄호가 닫힐수없는경우
                else:
                    answer.append(val)
            # val가 열린괄호면 무적권 넣어야함
            else:
                answer.append(val)
    # answer리스트 안에 괄호가 남아있을때
    if answer:
        return False
    else:
        return True


print(solution(s))