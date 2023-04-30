phone_number = "027778888"

def solution(phone_number):
    answer = (len(phone_number)-4)*"*"+phone_number[len(phone_number)-4:]
    return answer