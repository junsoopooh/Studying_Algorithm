# 1차 62.9/100
def solution(m, musicinfos):
    answer = ""
    answer_t = 0
    for x in musicinfos:
        start, end, title, content = x.split(",")
        start_h, start_m = start.split(":")
        end_h, end_m = end.split(":")
        playtime = 60 * (int(end_h) - int(start_h)) + (int(end_m) - int(start_m))
        tmp = list(content)
        while len(tmp) < playtime:
            tmp += list(content)
        for i in range(len(tmp) - len(m)):
            k = "".join(tmp[i : i + len(m)])
            if k == m:
                if i + len(m) + 1 < len(tmp) and tmp[i + len(m)] != "#":
                    if not answer_t:
                        answer = title
                        answer_t = playtime
                    else:
                        if answer_t < playtime:
                            answer = title
    return answer
