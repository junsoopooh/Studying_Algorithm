def solution(begin, end):
    answer = []
    for n in range(begin,end+1):
        num = 1
        if n == 1:
            num = 0
        for i in range(2,int(n**(0.5))+1):
            if not n%i:
                if n//i <= 10000000:
                    num = n//i
                    break
                else:
                    num = i
        answer.append(num)
    return answer