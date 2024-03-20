from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0  # 경과 시간 초기화
    bridge = deque([0] * bridge_length)  # 다리 상태를 나타내는 덱 초기화: 다리 길이만큼 0으로 채워진 덱
    truck_weights = deque(truck_weights)  # 대기 트럭 리스트를 덱으로 변환

    currentWeight = 0  # 현재 다리 위의 총 무게 초기화
    while len(truck_weights) > 0:  # 대기 트럭이 없을 때까지 반복
        time = time + 1  # 시간 증가

        currentWeight = currentWeight - bridge.popleft()  # 다리에서 나가는 트럭의 무게를 빼줌

        if currentWeight + truck_weights[0] <= weight:  # 다음 트럭이 다리에 진입할 수 있는지 확인
            currentWeight = currentWeight + truck_weights[0]  # 다리에 진입한 트럭의 무게를 추가
            bridge.append(truck_weights.popleft())  # 다리에 진입한 트럭을 덱에 추가

        else:
            bridge.append(0)  # 다음 트럭이 진입할 수 없으면 0을 추가하여 빈 자리를 유지함

    time = time + bridge_length  # 마지막 트럭이 다리를 빠져나가는 시간을 고려하여 경과 시간 업데이트

    return time  # 총 소요된 시간 반환
