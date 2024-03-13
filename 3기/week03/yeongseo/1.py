def solution(a, b):
        
    if a == b:
        return a
    
    if a < b: # a가 b보다 크게
        c = b
        b = a
        a = c

    if (a - b + 1) % 2 == 0: # 개수가 짝수
        return ((a - b + 1)*(a+b)) // 2
    else:
        return ((a - b)*(a+b)) // 2 + ((a+b) // 2)


print(solution(3,5))