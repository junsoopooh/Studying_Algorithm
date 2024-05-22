# [카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842)

def solution(brown, yellow):
    answer = []
    arr = []
    # 가로길이와 세로길이에서 모두 2를 빼고 곱한 값이 노란색 카펫의 개수와 같아야 한다.
    for i in range(1, int((yellow)**0.5)+1):
        if not yellow % i:
            arr.append([i, yellow//i])

    # 따라서 위에서 구한 값에 2를 더하면 카펫의 가로 길이와 세로 길이가 된다.
    # 모든 칸의 갯수를 구한 후 노란색 카펫의 갯수를 빼면 갈색 카펫의 갯수가 나온다.
    # 가로가 길어야 하므로 y, x 순으로 정렬한다.
    for x, y in arr:
        x += 2
        y += 2
        if x*y - yellow == brown:
            answer = [y, x]
    return answer
