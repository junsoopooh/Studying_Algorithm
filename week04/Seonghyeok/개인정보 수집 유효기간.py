def solution(today, terms, privacies):
    answer = []
    infoDict = dict()

    for i in terms:
        tmp = i.split(" ")
        infoDict[tmp[0]] =tmp[1]
    for idx,privacy in enumerate(privacies):
        privacy = privacy.split(" ")

        # 약관종류에 맞는 유효기간
        targetTerms = int(infoDict[privacy[1]])

        # 유효기간 + 개인정보 수집 일자 -> 비교대상
        ymd = privacy[0].split(".")
        y,m,d = int(ymd[0]),int(ymd[1]),int(ymd[2])
        m = m + targetTerms
        if m > 12:
            while 1:
                if m <= 12:
                    break
                m = m - 12
                y += 1

        y,m,d = str(y),str(m),str(d)
        # 오늘 날짜와 target 비교
        if len(m) == 1:
            m = '0'+ str(m)
        if len(d) == 1:
            d = '0'+ str(d)

        targetNums = int(y+m+d)
        todayNums = int(today.split(".")[0] +today.split(".")[1] + today.split(".")[2])

        print('targetNums : ',targetNums,'todayNums : ',todayNums)
        if targetNums <= todayNums:
            answer.append(idx+1)



    return answer



print(solution("2020.04.16", ["A 36", "S 4"], ["2017.04.17 A", "2014.04.16 S"]))