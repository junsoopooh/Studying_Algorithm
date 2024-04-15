def solution(clothes):
    
    dic = {}
    
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
    
    ans = 1
    
    for key in dic.keys():
        val = dic[key]
        if val > 0:
            ans *= (val + 1)
    
    return ans -1  # 다 벗는 경우 제외

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	)