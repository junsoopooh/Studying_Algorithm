import heapq
def solution(scoville,k):
    heapq.heapify(scoville)
    
    round = 0
    while True:
        if len(scoville) == 1:
            last =  heapq.heappop(scoville) # 마지막 애를 꺼내놓고 비교해야 함!
            if last < k:
                return -1
            else:
                return round
                    
        a = heapq.heappop(scoville)
        if a >= k:
            break 
        b = heapq.heappop(scoville)

        
        heapq.heappush(scoville, a + 2 * b)
        
        round += 1
    
    return round
    