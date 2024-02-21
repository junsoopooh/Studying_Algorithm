## 신고 결과 받기

def solution(id_list, report, k):
    n = len(id_list)
    answer = [0 for _ in range(n)]
    table = [[0 for _ in range(n)] for _ in range(n)]
    
    for x in report:
        sender, receiver = x.split()
        a = id_list.index(sender)
        b = id_list.index(receiver)
        table[b][a] = 1
        
    for i in table:
        if sum(i) >= k:
            for j in range(len(i)):
                if i[j]:
                    answer[j] += 1
            
    return answer