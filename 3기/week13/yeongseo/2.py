def solution(answers): 
    ans1 = [1, 2, 3, 4, 5]
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    ans = [[0, 1] , [0, 2] , [0, 3]]
    
    for i in range(len(answers)):
        if ans1[i % len(ans1)] == answers[i]:
            ans[0][0] += 1
        
        if ans2[i % len(ans2)] == answers[i]:
            ans[1][0] += 1 
        
        if ans3[i % len(ans3)] == answers[i]:
            ans[2][0] += 1
        
    ans.sort(key = lambda x : x[0], reverse = True)
    
    idx = 1
    real_ans = [ans[0][1]]
    
    while idx < len(ans):
        if ans[idx][0] == ans[0][0]:
            real_ans.append(ans[idx][1])
        
            idx += 1
        else:
            break
    
    real_ans.sort()
    return real_ans
        