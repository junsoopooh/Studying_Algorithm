'''
채점 결과
정확성: 85.7
합계: 85.7 / 100.0
'''

def solution(m, musicinfos):
    answer = ''

    # 재생된 음악시간과 answer를 넣는 리스트
    resultList = []

    for i in range(len(musicinfos)):
        # ,로 구분하여 리스트로 변경
        music = list(musicinfos[i].split(','))

        # 시간과 분을 나누기 위해
        tmpMusic1 = music[0].split(':')
        tmpMusic2 = music[1].split(':')

        # 시간
        hour = int(tmpMusic2[0]) - int(tmpMusic1[0])

        # 분
        minute = int(tmpMusic2[1]) - int(tmpMusic1[1])

        # 분으로 나타낸 실제 재생 시간
        resultTime = (hour * 60) + minute

        # 네오가 기억하는 시간(전체 길이에서 #을 뺌)
        lenMusic = len(music[3]) - music[3].count('#')

        # 실제 재생 시간이 기억하는 시간보다 길다면
        if resultTime > lenMusic:
            # 실제 시간에서 기억하는 시간을 빼주고
            tmpNum = resultTime - lenMusic

            remainder = tmpNum % lenMusic  # 나머지
            quotient = tmpNum // lenMusic  # 몫

            tmp = music[3][:quotient - 1]

            # 전체 음악 길이 시간만큼 붙여줌
            music[3] += ((music[3] * quotient) + tmp)

        # target이 일치하면
        if m in music[3]:
            idx = music[3].index(m)
            # 결과 리스트에 추가
            resultList.append([music[2], resultTime])

            # 뒤에 '#'이 붙은 경우는 빼줌 (ex - ABC#인데 착각되는 경우)
            if music[3][len(m) + idx:len(m) + idx + 1] == '#':
                resultList.pop()

    # 조건이 일치하는 음악이 없을때
    if len(resultList) == 0:
        return "(None)"
    else:
        # 조건과 일치하는 음악이 하나 일때
        if len(resultList) == 1:
            return resultList[0][0]
        else:
            # 재생된 시간이 제일 긴 음악
            resultList.sort(key=lambda x: x[1])
            return resultList[-1][0]

