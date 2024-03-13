def next(num):
    if num % 2 == 0:
        return num // 2
    else:
        return (num + 1) // 2

def solution(n,a,b):
    round_cnt = 1
    while True:
        # 종료조건 - 일단 기본적으로 둘이 붙어있어야(하나차이) 하고, 붙어있다고 꼭 싸우는건아님
        if abs(a-b) == 1:
            if max(a,b) % 2 != 1: # 큰수가 짝수일때만 붙음(5,6은 같은라운드 / 6,7은 다른 라운드)
                break
                
        
        round_cnt += 1
        
        a = next(a)
        b = next(b)
    
    return round_cnt
        