# [전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577)
def solution(phone_book):
    answer = True
    arr =dict() 
    for phone_number in phone_book:
        arr[phone_number] = True

    for phone_number in phone_book:
        tmp=""
        for num in phone_number:
            tmp +=num  
            if tmp in arr and tmp!=phone_number:
                answer = False

    return answer
