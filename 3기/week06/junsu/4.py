# [가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746)

# 1차시도 실패
# 가장 앞에있는 수가 크면 되지않을까?
# 십의 자리수가 같으면 우짤래?
def check_first(s):
    if len(str(s)) == 1:
        return int(s)
    else:
        return int(str(s)[0])

def solution(numbers):
    n = len(numbers)
    answer = ''
    arr = []
    for _ in range(10):
        arr.append([])
    for num in numbers:
        tmp = check_first(num)
        arr[num].append(num)
        
    return answer


# 2차시도 40/100
# 길이는 중요하지 않다.
# 3과 30 중 3이 먼저온다.
# 길이가 2인 애들 중 뒷자리가 앞자리보다 작은 애들은 나중에 와야함
# 높은 애들은 먼저와야함.
# 같은애들은? 그 다음을 따지면 된다.
# 3자리가 아닌 애들은 앞에를 붙여 3자리로 만들고 비교해주자.
def solution(numbers):
    answer = ''
    arr = []
    for i in range(len(numbers)):
        number = numbers[i]
        tmp = str(number)
        if len(tmp) == 1:
            arr.append([tmp+tmp+tmp,i])
            print()
        elif len(tmp) == 2:
            arr.append([tmp+tmp[0],i])
        else:
            arr.append([tmp,i])
    arr.sort(reverse=True)
    for x in arr:
        answer += str(numbers[x[1]])
    return answer

# 3차시도 93.3/100
# 343, 34 중 먼저 와야하는 것은?
# 3자리로 만들면 343, 343 똑같다.
#  만약343, 34, 1이 있다고 가정하면
# 343341 : 343,34,1 순서
# 343431 : 34,343,1 순서 (정답)
# 따라서 34가 먼저워야한다.
# 더 정확한 비교를 위해 3자가 아닌 4자로 만들어주자.
# 3433 과 3434로 비교하면 된다.
def solution(numbers):
    answer = ''
    arr = []
    for i in range(len(numbers)):
        number = numbers[i]
        tmp = str(number)
        if len(tmp) == 1:
            arr.append([tmp+tmp+tmp+tmp,i])
            print()
        elif len(tmp) == 2:
            arr.append([tmp+tmp,i])
        else:
            arr.append([tmp+tmp[0],i])
    arr.sort(reverse=True)
    for x in arr:
        answer += str(numbers[x[1]])
    return answer

# 4차시도 100/100
def solution(numbers):
    if not sum(numbers):
        return str(0)
    answer = ''
    arr = []
    for i in range(len(numbers)):
        number = numbers[i]
        tmp = str(number)
        if len(tmp) == 1:
            arr.append([tmp+tmp+tmp+tmp,i])
            print()
        elif len(tmp) == 2:
            arr.append([tmp+tmp,i])
        else:
            arr.append([tmp+tmp[0],i])
    arr.sort(reverse=True)
    for x in arr:
        answer += str(numbers[x[1]])
    return answer