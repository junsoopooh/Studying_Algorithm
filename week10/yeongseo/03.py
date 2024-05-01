def solution(progresses, speeds): 
    progresses = progresses[::-1] # 뒤집어서 스택처럼 사용
    speeds = speeds[::-1] 
    ans = []
    last_idx = len(progresses) - 1

    while True:
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        
        vapor = 0
        while True: # 스택 빼기...인데 위의 for문이 정상적으로 작동하려면 Progresses의 길이를 변동시키면 안되므로, Last_idx로 스택 길이 조정
            if last_idx >= 0 and progresses[last_idx] >= 100:
                last_idx -= 1
                vapor += 1
            else:
                break
        
        if vapor > 0:
            ans.append(vapor)
        
        if last_idx < 0:
            break
        
    return ans
                
            
            
    
    
