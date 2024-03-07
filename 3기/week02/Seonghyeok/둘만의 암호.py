alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def solution(s, skip, index):
    answer = ''
    for st in skip:
        alpha.remove(st)

    for i in s:
        alphaIdx = (alpha.index(i) + index)
        answer += alpha[alphaIdx % len(alpha)]

    return answer