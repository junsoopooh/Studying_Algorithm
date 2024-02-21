# 신규 아이디 추천

def solution(new_id):
    arr = ['1','2','3','4','5','6','7','8','9','0','-','_','.']
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    tmp = []
    for i in new_id:
        if  i.islower() == True or i in arr:
            tmp.append(i)
    new_id = ''.join(tmp)
    
    # 3단계
    if len(new_id) >1:
        tmp = []
        for i in range(len(new_id)-1):
            if new_id[i] == '.' and new_id[i+1] == '.':
                continue
            tmp.append(new_id[i])
        tmp.append(new_id[-1])
        new_id = ''.join(tmp)
        
    # 4단계
    if new_id:
        if new_id[0] == '.':
            if len(new_id) == 1:
                new_id = ''
            else:
                new_id = new_id[1:]
        
    # 4단계
    if new_id:
        if new_id[-1] == '.':
            if len(new_id) == 1:
                new_id = ''
            else:
                new_id = new_id[:len(new_id)-1]

        
    # 5단계
    if new_id == '':
        new_id = 'a'
        
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        
    # 6단계
    if new_id[-1] == '.':
        new_id = new_id[:len(new_id)-1]
        
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]
    
    return new_id