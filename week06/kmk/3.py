"""
n진수 게임
문제: https://school.programmers.co.kr/learn/courses/30/lessons/17687
"""
"""
1. 변환할 배열 생성하는데 구해야 할 숫자를 고려해 참가자수의 최대를 곱해서 생성해줌
2. 10~15는 미리 딕셔너리에 생성
3. 진법 변환 이 부분 다른 진수도 2진수처럼 변환시켜주면 됨. 단, 나머지가 10~15이면 딕셔너리에 보관된 값 넣어줌
4. 인덱스 접근을 위해 p는 1빼주고 시작하고 모든 숫자를 변환할 필요없이 그냥 t개되면 break
"""

def solution(n, t, m, p):

    nums = [i for i in range(t * 100)]

    dic = dict(zip([i for i in range(10, 16)], ["A", "B", "C", "D", "E", "F"]))

    def trans(num, n):
        if num == 0:
            return "0"

        val = ""

        while num:
            val += dic[num % n] if num % n >= 10 else str(num % n)
            num //= n

        return val[::-1]

    string = ""
    ans, p = "", p - 1

    for num in nums:
        string += trans(num, n)
        if len(string) > p:
            ans += string[p]
            p += m
        if len(ans) == t:
            break

    return ans