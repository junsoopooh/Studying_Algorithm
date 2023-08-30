# 영어 끝말잇기 문제
def solution(n, words):
    flag = False
    ans_1 = 1
    ans_2 = 0
    for i in range(1, len(words)):
        if flag:
            break
        ans_1 += 1
        if ans_1 > n:
            ans_1 -= n
        ans_2 = i//n + 1
        if words[i-1][-1] != words[i][0]:
            flag = True
            break
        for j in range(i):
            if words[j] == words[i]:
                flag = True
                break
    if not flag:
        ans_1 = ans_2 = 0
    answer = [ans_1, ans_2]
    return answer
