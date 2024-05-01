from itertools import combinations

def solution(orders, course):
    count_dic = {}
    
    for order in orders:
        for i in course:
            combi = list(combinations(order, i)) # 가능한 모든 조합 다 생성
            for comb in combi:
                comb = list(comb) 
                comb.sort() # 튜플은 정렬이 안돼서 리스트로 변경하고 정렬
                comb = ''.join(comb)
                if comb in count_dic.keys(): # 조합과 ,해당 조합이 나온 횟수를 딕셔너리에 기록
                    count_dic[comb] += 1
                else:
                    count_dic[comb] = 1 
    
    ans = []
    
    for c in course:
        chosen_dic = {} # c개수의 메뉴의 선택도(몇번 선택됐는지가 키, 메뉴 조합이 값)를 나타내는 딕셔너리
        max_chosen = 0
        
        for key in count_dic.keys():
            if len(key) == c: # c개수에 적합하는 조합이면
                if count_dic[key] >= max_chosen:
                    max_chosen = count_dic[key] # 가장 많이 나온 조합 수 업데이트
                    # c길이의 메뉴 중에 선택 횟수가 겹치는 경우가 있으므로 딕셔너리에 리스트로 {선택 횟수 : [선택된, 메뉴, 리스트]} 이렇게 기록
                    if max_chosen in chosen_dic.keys():
                        chosen_dic[max_chosen].append(key) 
                    else:
                        chosen_dic[max_chosen] = [key]
                        
        if max_chosen > 1: # 두명 이상에게 선택된 조합만
            ans += chosen_dic[max_chosen]
    
    ans.sort()
    return ans
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))