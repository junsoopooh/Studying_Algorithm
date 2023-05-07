numbers = [5,8,4,0,6,7,9]

def solution(numbers):
    all_sum = sum(x for x in range(10))
    return all_sum - sum(numbers)

print(solution(numbers))