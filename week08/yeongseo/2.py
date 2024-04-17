def solution(n, stages):
    max_stage = max(stages)
    dic = [[0,0] for i in range(n+1)] # 도달 but 클리어 노 / 도달한 플레이어
    
    for i in stages:
        if i == n+1:
            for stage in range(1, n+1):
                dic[stage][1] += 1 # 모두 다 도달 1씩 더해줌
        
        else:
            dic[i][0] += 1 # 클리어 노
            for stage in range(1, i+1):
                dic[stage][1] += 1 # 나 전까지 도달한 플레이어
    
    ans = []
    for idx, val in enumerate(dic):
        if idx != 0:
            if val[1] != 0:
                ans.append([idx, val[0] / val[1]])
            else:
                ans.append([idx, 0]) # 도달한자 없을때 실패율은 0
    
    ans.sort(key = lambda x : -x[1])
    real_ans = []
    for i in ans:
        real_ans.append(i[0])
    
    return real_ans
        
    
    
print(solution(4, 	[4,4,4,4,4]))