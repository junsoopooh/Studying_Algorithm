"""
옹알이 (2)
https://school.programmers.co.kr/learn/courses/30/lessons/133499
"""


def solution(babbling):
    ans = 0

    def check(b):
        for n in ["11", "22", "33", "44"]:
            if n in b:
                return False
        return True

    for b in babbling:
        b = b.replace("aya", "1").replace("ye", "2").replace("woo", "3").replace("ma", "4")
        if b.isdigit() and check(b):
            ans += 1

    return ans