# 74
def solution(name):
    leng = len(name)
    min_change = [min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name] # 위 또는 아래로 갈 시의 최소 이동횟수
    answer = 0 
    idx = 0 
    
    while True:
        # 변경해주고, 변경했으니 해당 위치의 최소 이동횟수 0으로 설정 
        answer += min_change[idx]
        min_change[idx] = 0
        
        # 모든 문자 'A'됐는지 체크
        if sum(min_change) == 0:
            break 
        
        # 좌/우 이동횟수 초기화
        left = 1
        right = 1
        
        # 바꿀게 있을때까지 좌 OR 우로 이동시킴
        while min_change[idx - left] == 0:
            left +=1 
        
        while min_change[idx + right] == 0:
            right += 1 
        
        if left < right:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right 
        
    return answer
            
# ??
def solution(name):
    # 알파벳 변경 횟수( 상하 이동 ) 
    spell_move = 0
    
    # 커서 이동 횟수, 이름의 길이 - 1( 좌우 이동 )
    cursor_move = len(name) - 1  
    
    for i, spell in enumerate(name):
        spell_move += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 아래 3가지 경우 중 최소 이동 값으로 갱신
        # 1. 이전 커서 이동 값 ( 초기값 - 이름의 길이 - 1 )
        # 2. 연속된 A의 왼쪽 시작
        # 3. 연속된 A의 오른쪽 시작
        cursor_move = min([ cursor_move, 2 * i + len(name) - next, i + 2 * (len(name) - next) ])
        
    # 조이스틱 조작 횟수 = 알파벳 변경 횟수( 상하 이동 ) + 커서 이동 횟수( 좌우 이동 )    
    return spell_move + cursor_move

