def solution(record):
    uid_nick_map = dict()
    ans = []
    
    for rec in record:
        if parse_nick(rec) != None: 
            uid, nick = parse_nick(rec)
            uid_nick_map[uid] = nick # 최종 닉네임 기록하기 위한 For 문... 거기서 딕셔너리에 uid-nick매핑 저장
        
    for rec in record:
        if parse(rec) != None:
            # 입장이냐 퇴장이냐에 따라 parse의 결과가 달라짐
            if len(parse(rec)) == 3:
                action, uid , nick = parse(rec)
                sent = sentence(action, uid, uid_nick_map)
            elif len(parse(rec)) == 2:
                action, uid = parse(rec)
                sent = sentence(action, uid, uid_nick_map)
            # change의 경우에는 sent가 없음
            if sent != "":
                ans.append(sent)
    
    return ans 

# 입장이나 변경의 경우에만 uid랑 nick을 리턴
def parse_nick(rec):
    tmp = rec.split(" ")
    if tmp[0] == "Enter" or tmp[0] == "Change":
        return [tmp[1], tmp[2]]
    else:
        return None

# 입장이나 퇴장의 경우에만 action, uid, (nick - 퇴장의 경우엔 없음) 리턴
def parse(rec):
    tmp = rec.split(" ")
    if tmp[0] == "Enter" :
        return [tmp[0], tmp[1], tmp[2]]
    elif tmp[0] == "Leave":
        return [tmp[0], tmp[1]]
    else:
        return None

def sentence(action, uid, uid_nick_map):
    if action == "Enter":
        return uid_nick_map[uid] + "님이 들어왔습니다."
    
    elif action == "Leave":
        return uid_nick_map[uid] + "님이 나갔습니다."
        
    # Change인 경우 아무것도 하지 않음
    else:
        return ""

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

# print("Enter uid nuzi".split(" "))