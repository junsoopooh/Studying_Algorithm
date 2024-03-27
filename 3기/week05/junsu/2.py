def solution(msg):
    answer = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    arr = dict()
    for i in range(len(alphabet)):
        arr[alphabet[i]] = i+1
        
    # 다음 추가될 색인 번호는 마지막보다 1 큰 수
    last_num = len(alphabet)+1
    # idx까지 볼때 idx-1 까지만 포함되므로 1로 설정
    idx = 1
    n = len(msg)
    
    while idx <= n:
        # 이미 있다면 다음이 더 긴지 확인하기 위해 idx만 1 증가
        if msg[:idx] in arr:
            idx += 1
            continue
        else:
            # 사전에 없다면, 길이가 1 작을 때가 가장 긴 단어이므로(2단계) 그 번호를 출력
            answer.append(arr[msg[:idx-1]])
            # 없는 단어와 색인 번호를 추가
            arr[msg[:idx]] = last_num
            # 다음 추가될 색인 번호 1 증가
            last_num += 1
            # 찾아낸 가장 긴 단어는 삭제
            msg = msg[idx-1:]
            # 인덱스 오류를 방지하기 위해 매 반복마다 길이 체크
            n = len(msg)
            # 인덱스 초기화
            idx = 1
            
    # 마지막 반복 때 사전에 있는 단어로 끝났다면 추가되지 않는 단어가 생기므로 추가
    # KAKAO에서 마지막 O는 별도로 추가해야함
    if msg:
        answer.append(arr[msg])
    return answer