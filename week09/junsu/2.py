def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stk = []
    for i in range(len(prices)):
        price = prices[i]
        if not stk:
            stk.append([price,i])
            continue
        while stk:
            now_price, now_time = stk[-1]
            if price < now_price:
                answer[now_time] = (i-now_time)
                stk.pop()
            else:
                break
        stk.append([price,i])
    if stk:
        while stk:
            p,t = stk.pop()
            answer[t] = len(prices)-1-t
    return answer