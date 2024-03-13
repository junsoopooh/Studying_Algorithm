
def solution(files):
    # [[헤드 , 넘버, 테일], [헤드 , 넘버, 테일]...]
    splited = []
    answer = []
    
    for file in files:
        idx = 0
        head = ""
        nums = ""
        tail = ""
        # 헤드 분리 # idx < len(file)로 인덱스에러 방지
        while idx < len(file) and ord(file[idx]) < ord("0") or ord(file[idx]) > ord("9"):
            head += file[idx]
            idx += 1
        
        # 숫자분리 # < ord("9")로 해서 계속 틀렸었음 # 최대 다섯개
        num_len = 0
        while idx < len(file) and num_len <= 5 and ord("0") <= ord(file[idx]) <= ord("9"):
            nums += file[idx]
            idx += 1
            num_len += 1
        
        # 꼬리 분리
        if idx < len(file):
            tail += file[idx:]
        
        splited.append([head, nums, tail])
    
    # 정렬 조건 1. 헤드 대소문자 상관없이, 2. 숫자부분str의 실제 숫자값
    splited.sort(key = lambda x : (x[0].lower(), int(x[1])))
            
    for sp in splited:
        answer.append("".join(sp))
    
    return answer