import math

def solution(m, musicinfos):
    answer = None

    # 치환
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace("B#", "b")

    for info in musicinfos:
        start, end, title, content = info.split(",")
        hour, minute = map(int, start.split(":"))
        start = hour * 60 + minute

        hour, minute = map(int, end.split(":"))
        end = hour * 60 + minute 
        duration = end - start # 총 재생 시간

        # 치환
        content = content.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace("B#", "b")

        # 총 재생 음표(중간에 끊긴거 포함해서) 
        content *= math.ceil(duration / len(content)) 
        content = content[:duration] # 를 재생시간만큼 자름 

        if m not in content:
            continue
        
        # 중간조건 : 재생시간이 젤 긴거 리턴해줘야 함 / 마지막 조건 : 재생된 시간도 같으면 먼저 입력된 음악 제목 반환
        if answer == None or answer[0] < duration or (answer[0] == duration and answer[1] > start):
            answer = (duration, start, title)
    
    if answer:
        return answer[-1]
        
    return "(None)"

solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]	)