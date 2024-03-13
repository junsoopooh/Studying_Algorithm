"""
[3차] 파일명 정렬
https://school.programmers.co.kr/learn/courses/30/lessons/17686
"""
"""
1. 정렬용 배열 초기화 / files를 들어온순서대로 딕셔너리 생성 {0: ?, 1:?}
2. 숫자로 구분해서 정렬용 배열에 [대소문자 구분없는 head, 숫자, 순서] 넣어준다.
3. 그대로 정렬하고 정답배열에 files[순서]의 value를 넣어주면 됨
"""

def solution(files):
    answer, criteria = [], []
    files = dict(enumerate(files))

    def extract(s):  # 숫자 추출
        num = ""
        for c in s:
            if c.isdigit():
                num += c
            if num and not c.isdigit():
                break
        return num

    for o, f in files.items():
        num = extract(f)  # 숫자 추출
        head = f.split(num)[0]  # 헤드 추출
        criteria.append([head.lower(), num, o])  # 헤드, 숫자, 순서

    criteria.sort(key=lambda x: (x[0], int(x[1]), x[2]))

    for a, b, c in criteria:
        answer.append(files[c])

    return answer