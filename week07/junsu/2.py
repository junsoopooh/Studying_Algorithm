# 성격 유형 검사

def solution(survey, choices):
    answer = []
    board = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    n = len(survey)
    for i in range(n):
        idx = survey[i]
        if choices[i] < 4:
            board[idx[0]] += abs(4-choices[i])
        elif choices[i] >4:
            board[idx[1]] += (choices[i]-4)
            
    if board['R'] >= board['T']:
        answer.append('R')
    else:
        answer.append('T')
        
    if board['C'] >= board['F']:
        answer.append('C')
    else:
        answer.append('F')
        
    if board['J'] >= board['M']:
        answer.append('J')
    else:
        answer.append('M')
        
    if board['A'] >= board['N']:
        answer.append('A')
    else:
        answer.append('N')
        
    return ''.join(answer)