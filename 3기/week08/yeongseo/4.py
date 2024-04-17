def solution(number, k):
    answer = []
    
    for num in number:
        # 스택에 원소가 있고, k가 0보다 크고, 현재 숫자가 스택의 마지막 숫자보다 크면
        # 스택의 왼쪽부터 큰 수여서, k가 소진될때까지 큰 수를 밀어넣는거
        while len(answer) > 0 and k > 0 and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    
    if k : 
        return number[:-k] # 54321 같은 경우 k가 소진될 수 없음

    else:
        return ''.join(answer)
        
solution("1924", 2)