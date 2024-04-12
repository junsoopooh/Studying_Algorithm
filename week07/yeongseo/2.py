def solution(babbling):
    answer = 0
    
    possible = ['aya', 'ye', 'woo', 'ma']
    
    for word in babbling:
        for posi in possible:
            if posi * 2 not in word:
                word = word.replace(posi, ' ')
        
        if word.isspace():
            answer += 1
    
    return answer