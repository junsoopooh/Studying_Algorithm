# [큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883))

def solution(number, k):
    stk = []
    
    for num in number:
        # stk가 비었으면 넣음
        if not stk:
            stk.append(num)
            continue
        if k > 0:
            # 지금 주목하는 수가 방금 넣은 수보다 크다면 뺸다.
            while stk[-1] < num:
                stk.pop()
                k -= 1
                # 더이상 뺄 것이 없거나 더이상 빼면 안되면 반복문 종료
                if not stk or k <= 0:
                    break
        stk.append(num)
        
    # 모두 순회했는데 아직 뺄것이 남았다면 가장 뒤에것만뺀다.
    if k:
        stk = stk[:-k]
        answer = ''.join(stk)
    else:
        answer = ''.join(stk)

    return answer