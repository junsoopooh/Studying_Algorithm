"""
방금 그 곡
https://school.programmers.co.kr/learn/courses/30/lessons/17683
"""
def solution(m, music):
    def time_diff(a, b): # 시간 처리 메소
        return int(b[:2]) * 60 + int(b[3:]) - int(a[:2]) * 60 - int(a[3:])

    ans, ans_diff = "", 0 # 정답, 정답일 때 재생시간

    m = m.replace("A#", "1").replace("G#", "2").replace("F#", "3").replace("D#", "4").replace("C#", "5")

    for info in music:
        s, e, t, a = info.split(",")
        a = a.replace("A#", "1").replace("G#", "2").replace("F#", "3").replace("D#", "4").replace("C#", "5")
        diff = time_diff(s, e)  # 재생시간
        if diff >= len(a):  # 재생시간이 악보보다 큰 경우
            tmp = a
            while diff >= len(a):  # 악보하고 비슷하거나 클때까지 복사
                a += tmp
        else:
            a = a[:diff]

        if m in a and diff > ans_diff:
            ans, ans_diff = t, diff

    return ans if ans else "(None)"