def solution(brown,yellow):
    whole = brown + yellow
    
    row = 0
    col = 0 
    
    for i in range(1, whole // 2 + 1):
        if whole % i == 0:
            # 진짜 가로 세로값이 될 수 있는지 확인하기 위해 두칸씩 줄여서 곱한 후 그것이 yellow가 되는지 확인 
            if i - 2 > 0 and yellow % (i - 2) == 0 and whole // i - 2 > 0 and yellow % (whole // i -2) == 0:
                row = max(i, whole //i )
                col = min(i, whole //i )
            
    
    return [row, col]
    