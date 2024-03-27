def solution(keymap, targets):
    answer = []
    arr = dict()
    idx = 0
    
    # 각 글자를 입력하기 위한 버튼 누르는 횟수의 최솟값을 저장하는 배열 arr을 만드는 과정
    # 각 버튼의 0번 index 부터 하나씩 참조
    while True:
        # 모든 키의 입력 범위를 넘어갔는지 확인하기 위한 플래그
        flag = False
        # 모든 버튼 순회
        for button in keymap:
            # 예를 들어, 버튼을 5번 누를 수 있는데 idx가 6이라면 그 버튼은 더이상 조사할 필요가 없으므로 넘어감
            if idx >= len(button):
                continue
            # 어떤 버튼을 참조했음을 플래그에 표시. 이 과정이 없으면 keymap중 가장 긴 버튼의 길이를 구하느 과정이 따로 필요
            flag = True
            # idx번 눌렀을 때 해당 버튼에서 입력되는 글자
            letter = button[idx]
            # 지금 입력되는 글자가, 아직 입력된적 없는 글자라면 배열에 추가
            if letter not in arr:
                arr[letter] = idx+1
            # 이미 입력된적 있다면, idx를 작은 값으로 바꿔줌. 각 글자를 누르는 최소 방법만 알면 되기 때문
            # 0번 인덱스는 1번 눌러야 하므로 idx+1을 저장
            else:
                arr[letter] = min(arr[letter],idx+1)
        # 아무 버튼도 탐색하지 않았다면 무한루프 종료
        if not flag:
            break
        idx += 1
        
    for target in targets:
        cnt = 0
        # 타겟을 하나씩 탐색하며 글자를 확인
        for i in range(len(target)):
            # 만약 글자를 입력할 방법이 있다면 해당 키의 값을 추가
            if target[i] in arr:
                cnt += arr[target[i]]
            # 글자를 입력할 방법이 없다면 -1로 지정하고 종료
            else:
                cnt = -1
                break
        answer.append(cnt)
    return answer