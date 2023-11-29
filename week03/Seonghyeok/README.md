# Week 01

## 문제 리스트

|          | 난이도  | 문제제목               | 혼자 풀었나요? |
|----------|------|--------------------|----------|
| 11/26(일) | Lv01 | 공원 산책 | O        |
| 11/29(수)|Lv02|3 x n 타일링|




## 각 문제풀이별 생각정리
### 1. 공원 산책
1. 공원을 2차원 배열로 초기화 해야함
2. S위치 인덱스를 찾아야함
3. op와 num으로 현재 인덱스 업데이트 <br>
3-1) 업데이트시 예외처리 ['X'가 나올경우 , 정해진 인덱스를 벗어난경우]
4. 위 방식으로 코드를 구현하니 50점임..
5. W 방향에서 '+'를 '-'로 잘못입력함 .. 아오 
```
def solution(park, routes):

    parkList = []
    target_index = 0
    # 공원을 나타내는 2차원 배열 초기화
    for i in park:
        parkList.append(list(i))

    # start index 찾기 
    for i in range(len(parkList)):
        for j, target in enumerate(parkList[i]):
            if target == 'S':
                target_index = [i, j]
                break

    # 행
    column = len(parkList[0]) 
    # 열
    row =  len(parkList)
    
    
    for val in routes:
        op = val[0]
        num = int(val[2])

        if op == 'E':
            for i in range(1,num+1):
                target_index[1] += 1
                if target_index[1] >= column:
                    target_index[1] -= i
                    break
                elif parkList[target_index[0]][target_index[1]] == 'X':
                    target_index[1] -= i
                    break
        elif op == 'W':
            for i in range(1, num+1):
                target_index[1] -= 1
                if target_index[1] < 0:
                    target_index[1] -= i
                    break
                elif parkList[target_index[0]][target_index[1]] == 'X':
                    target_index[1] += i
                    break
        elif op == 'S':
            for i in range(1, num+1):
                target_index[0] += 1
                if target_index[0] >= row:
                    target_index[0] -= i
                    break
                elif parkList[target_index[0]][target_index[1]] == 'X':
                    target_index[0] -= i
                    break
        elif op == 'N':
            for i in range(1, num+1):
                target_index[0] -= 1
                if target_index[0] < 0:
                    target_index[0] += i
                    break
                elif parkList[target_index[0]][target_index[1]] == 'X':
                    target_index[0] += i
                    break


    return target_index


```


