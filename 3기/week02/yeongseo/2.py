

def increment(ch, idx, skip):
    order = ord(ch)
    cnt = 0
    while cnt < idx: # skip문자 제외하고 index만큼 건너뛸때까지
        order += 1
        if order > ord('z'): # z넘어가면 a로 돌아가게, 이걸 order += 1 바로 뒤에 둬야만 skip할때 스킵할 문자인지 제대로 판단가능
            order = order - ord('z') + (ord('a') -1 )

        if chr(order) in skip: # 건너뛴거로 치지 않음 
            continue
        
        cnt += 1 # 건너뛴거로 침 
    
    return chr(order) # 변경된 숫자

def solution(s, skip, index):
    arr = [i for i in s]
    skip = set(skip)
    for i in range(len(arr)):
        ch = arr[i]
        new_ch = increment(ch, index, skip) # 변경할 문자 찾는 함수

        arr[i] = new_ch

    answer = ''.join(arr)
    return answer

print(solution("ybcde", "az", 1))