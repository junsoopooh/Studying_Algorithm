# 공원 산책

def solution(park, routes):
    H = len(park)
    W = len(park[0])
    a = 0
    b = 0    
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                a = i
                b = j
    def check(p,q,x,y):
        for i in range(1,q+1):
            if p == 'N':
                if x-i < 0 or park[x-i][y] == 'X':
                    return False
            elif p == 'S':
                if x+i >= H or park[x+i][y] == 'X':
                    return False
            elif p == 'E':
                if y+i >= W or park[x][y+i] == 'X':
                    return False
            elif p == 'W':
                if y-i < 0 or park[x][y-i] == 'X':
                    return False
        if p == 'N':
            return x-q,y
        elif p == 'S':
            return x+q,y
        elif p == 'E':
            return x,y+q
        elif p == 'W':
            return x,y-q
    i = 0
    while i < len(routes):
        way_to_go, distance_to_go = routes[i].split()
        if not check(way_to_go,int(distance_to_go), a,b):
            i += 1
            continue
        a,b = check(way_to_go,int(distance_to_go), a,b)
        i += 1
    return [a,b]
