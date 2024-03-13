from collections import Counter
def solution(participant, completion): 
    counter = Counter(participant)
    for name in completion:
        if counter[name]:
            counter[name] -= 1
    
    for k, v in counter.items():
        if v != 0:
            return k 
    