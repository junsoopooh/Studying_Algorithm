## 문제 리스트

|          | 난이도  | 문제제목     | 혼자 풀었나요? |
|----------|------|----------|----------|
| 03/03(일) | Lv01 | 하샤드 수    | O        |
| 03/03(일) | Lv01 | 둘만의 암호   | O        |
| 03/05(월) | Lv02 | 점프와 순간이동 | X        |
| 03/04(일) | Lv02 | 방금 그곡    | X        |






## 각 문제풀이별 생각정리
### 1. 하샤드 수
X
### 2. 둘만의 암호
1. skip에 포함된 string 값들을 제외한 알파벳 배열(alpha) 만듦
2. 주어진 s의 각 문자열의 alpha 안에서 갖는 index 구함(alphaIndex)
3. alpha[alphaIndex + index]값 == target 문자열</p>
3-1.alphaIndex + index 값이 len(alpha)보다 크면 첫 인덱스로 돌리게 -len(alpha) 진행</p>
결과 : 테스트 3,17,18,19 통과 X
```
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def solution(s, skip, index):
    answer = ''
    for st in skip:
        alpha.remove(st)
    
    
    for i in s:
        alphaIdx = alpha.index(i)
        if alphaIdx+index < len(alpha)-1:
            answer += alpha[alphaIdx+index]
        else:
            answer += alpha[(alphaIdx+index) - len(alpha)]

    return answer
```
4. index = 20일 경우 생각 -> index error
5. 나머지 연산을 통해서 해결방안 구함
```        
alphaIdx = (alpha.index(i) + index)
answer += alpha[alphaIdx % len(alpha)]
```

### 3. 점프와 순간이동
1. 처음에 t = (n+1) * 2**k (k >= 0)와 같은 개같은 식을 세워 진행
2. 어림도 없지 안됨
3. 답지 봄
4. n이 홀수일 때 n = n-1을 하고, n이 짝수일 때 n = n // 2를