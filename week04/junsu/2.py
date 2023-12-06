# 개인정보 수집 유효기간
# 나의 풀이(40점)
# 뭐가 틀렸는데...
def solution(today, terms, privacies):
    answer = []
    today_y, today_m, today_d = today.split('.')
    today_y = int(today_y)
    today_m = int(today_m)
    today_d = int(today_d)
    def check(y,m,d,t):
        ans = True
        m += t
        if m >12:
            y += 1
            m -= 12
            
        if y > today_y:
            ans = False
        elif y == today_y:
            if m > today_m:
                ans = False
            elif m == today_m:
                if d > today_d:
                    ans = False
        return ans
        
    arr = dict()
    for x in terms:
        term_type, term_months = x.split()
        arr[term_type] = int(term_months)
    for i in range(len(privacies)):
        privacy_date, privacy_type = privacies[i].split()
        privacy_y, privacy_m, privacy_d = privacy_date.split('.')
        tmp = check(int(privacy_y),int(privacy_m),int(privacy_d),arr[privacy_type])
        if tmp:
            answer.append(i+1)
    return answer

# 
