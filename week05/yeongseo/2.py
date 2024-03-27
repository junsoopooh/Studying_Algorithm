def solution(msg):
    answer = []
    lzw_dic = {}
    for i in range(1, 27):
        lzw_dic[chr(ord('A') + i - 1)] = i
        
    last_val = 26
    lo = 0
    hi = 1
    while hi <= len(msg):
        if msg[lo:hi] not in lzw_dic:
            answer.append(lzw_dic[msg[lo:hi - 1]])
            last_val += 1
            lzw_dic[msg[lo:hi]] = last_val
            lo = hi - 1
        
        hi += 1

    answer.append(lzw_dic[msg[lo:hi - 1]])
    return answer


# 70점
def solution(msg):
    answer  = []
    lzw_dic = {}
    for i in range(1, 27):
        lzw_dic[chr(ord('A') + i - 1)] = i
        
    last_val = 26
    
    lo = 0
    hi = 1
    while hi < len(msg):
        while hi < len(msg) and msg[lo:hi] in lzw_dic.keys():
            hi += 1
        
        if hi >= len(msg):
            break
        answer.append(lzw_dic[msg[lo:hi-1]])
        last_val += 1
        if hi < len(msg):
            lzw_dic[msg[lo:hi]] = last_val

        
        lo = hi -1 

    if msg[lo:hi] in lzw_dic.keys():
        answer.append(lzw_dic[msg[lo:hi]])
    else:
        answer.append(lzw_dic[msg[-1]])
            
    return answer

print(solution("KAKAO"))