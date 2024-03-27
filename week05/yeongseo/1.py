def solution(keymap, targets):
    answer = []
    
    keymap_dic = {}
    for kmap in keymap:
        for idx, v in enumerate(kmap):
            if v in keymap_dic.keys():
                if keymap_dic[v] > idx + 1:
                    keymap_dic[v] = idx + 1 # 최소회수만 기록하기 위해
            else:
                keymap_dic[v] = idx + 1
    
    for target in targets:
        cost = 0 
        for t in target:
            if t not in keymap_dic.keys():
                cost = -1
                break
            else:
                cost += keymap_dic[t]
        answer.append(cost)
    
    return answer