from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 1
    
    bridge = deque([[0, truck_weights[0], 0]]) # 트럭 인덱스 , 트럭 무게, 다리에서의 위치
    cur_weight = truck_weights[0]
    next_truck_idx = 1
    
    while bridge:
        # 다리 위의 트럭들은 한칸씩 증가시키고, 맨 마지막 애는 다리에서 나올때가 되면 나오게 해줌
        if len(bridge) > 0 and bridge[-1][2] + 1 >= bridge_length:
            cur_weight -= bridge[-1][1]
            bridge.pop()
        
        for truck in bridge:
            truck[2] += 1
        
        # 다리에 올릴 트럭이 존재하고, 트럭이 다리의 최대 개수를 넘지 않고, 트럭이 다리의 최대 무게를 넘지 않으면 트럭을 다리에 올림
        if next_truck_idx < len(truck_weights) and len(bridge) + 1 <= bridge_length and cur_weight + truck_weights[next_truck_idx] <= weight:
            bridge.appendleft([next_truck_idx, truck_weights[next_truck_idx] ,0])
            cur_weight += truck_weights[next_truck_idx]
            next_truck_idx += 1
        
        answer += 1
        
    return answer
        
print(solution(2,10,[7,4,5,6]))