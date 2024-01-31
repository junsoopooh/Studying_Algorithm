def solution(s):
    lst = s.split(' ')
    answer = ''
    for i in range(len(lst)):
        word = list(lst[i])
        for idx, target in enumerate(word):
            if idx == 0 and target.islower():
                word[idx] = target.upper()
            elif idx != 0 and target.isupper():
                word[idx] = target.lower()
        if i == len(lst) - 1:
            answer += ''.join(word)
        else:
            answer += ''.join(word)
            answer += ' '
    return answer
