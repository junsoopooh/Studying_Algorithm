def jinsu(n,q): # n의 q진수 구한다
    rev_base = ''
    
    mode_dict = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}

    while n > 0:
        n, mod = divmod(n, q)
        if mod > 9:
            mod = mode_dict[mod]
        rev_base += str(mod)

    return rev_base[::-1]

def solution(n, t, m, p):
    count = 1     # count의 n진수를 구할거임
    numbers = "0"
    while True:
        a = jinsu(count, n) # count의 n진수는 a
        for i in a: # a의 값들을 하나씩 numbers에 넣음
            numbers += i
            if len(numbers) >= m*t: # 이 값이 참가인원*미리 구할 숫자의 개수 를넘어가면
                break # for문탈출
                
        count += 1 # 다음 십진수count로 하나 더해줌
        if len(numbers) >= m*t: # 값이 범위 벗어나면 while 탈출
            break
        
    result = "" 
    num_list = list(numbers) # 인덱싱을 위해 리스트로 변환
    while len(result)  < t: # 순서에 따라 값 넣기 위해 1~ numbers길이의 범위 설정
        result += num_list[p-1]
        p += m
        
    return result    
