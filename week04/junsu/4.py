# 다리를 지나는 트럭 https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 1차 42.9/100
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    in_bridge = deque()
    for _ in range(bridge_length):
        in_bridge.append(0)
    for truck in truck_weights:
        while sum(in_bridge)+truck > weight:
                outgoing_truck = in_bridge.popleft()
                in_bridge.append(0)
                answer += 1
                if outgoing_truck:
                    answer -= 1
        if sum(in_bridge)+truck <= weight:
            in_bridge.popleft()
            in_bridge.append(truck)   
            answer += 1
    for i in range(len(in_bridge)-1,-1,-1):
        if in_bridge[i]:
            answer += (i+1)
            break
    return answer

# 2차 92.9/100
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    in_bridge = deque()
    for _ in range(bridge_length):
        in_bridge.append(0)
    idx = 0
    while idx < len(truck_weights):
        answer += 1
        in_bridge.popleft()
        if sum(in_bridge) + truck_weights[idx] <= weight:
            in_bridge.append(truck_weights[idx])
            idx += 1
        else:
            in_bridge.append(0)
            
    for i in range(len(in_bridge)-1,-1,-1):
        if in_bridge[i]:
            answer += (i+1)
            break
    return answer

# 3차 100/100
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    in_bridge = deque()
    for _ in range(bridge_length):
        in_bridge.append(0)
    idx = 0
    total_weight = 0
    while idx < len(truck_weights):
        answer += 1
        total_weight -= in_bridge.popleft()
        if total_weight + truck_weights[idx] <= weight:
            in_bridge.append(truck_weights[idx])
            total_weight += truck_weights[idx]
            idx += 1
        else:
            in_bridge.append(0)
            
    for i in range(len(in_bridge)-1,-1,-1):
        if in_bridge[i]:
            answer += (i+1)
            break
    return answer