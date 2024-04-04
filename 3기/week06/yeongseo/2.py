def solution(dartResult):
    nums = [str(i) for i in range(0, 11)]
    starcha = ["*", "#"]
    dartResult = dartResult.replace("10", "t")
    
    res = []
    
    score = 0
    
    for i in dartResult:
        if i in nums:
            score += int(i)
            continue
        elif i == "t":
            score += 10
            continue
        elif i == 'S':
            res.append(score)
        elif i == 'D':
            res.append(score ** 2)
        elif i == 'T':
            res.append(score ** 3)
        elif i == '*':
            if len(res)>1:
                res[-1] *= 2  
                res[-2] *= 2  
            else : 
                res[-1] *= 2
        elif i == '#':
            res[-1] *= -1
        
        score = 0 # 점수 초기화
    
    return sum(res)
