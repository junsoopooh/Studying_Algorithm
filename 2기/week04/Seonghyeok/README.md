# Week 01

## 문제 리스트

|          | 난이도  | 문제제목   | 혼자 풀었나요? |
|----------|------|--------|----------|
| 12/04(월) | Lv01 | 짝수와 홀수 | O        |
|12/06(수)|Lv01|개인정보 수집 유효기간|O|




## 각 문제풀이별 생각정리
### 1. x 만큼 간격이 있는 n개의 숫자
X
### 2. 개인정보 수집 유효기간

Point 유효기간(정해준) 전,후
2021.01.05 수집 - 2022.01.04 마감,2022.01.05파기
    
1. terms를 dictionary 형태로 바꿔서 진행해야겠다.<br>
1-1. 약관 종류에따르는 유효기간을 빠르게 얻기위해 ?
2. privacies를 반복문 돌리면서(enumerate)<br>
2-1. 반복문 조건에 맞는 값들의 인덱스 추출하여 answer에 추가<br>
2-2. 12월이 넘어갈때의 조건은 일단 더하고 12 넘어가면 m은 -12 y는 + 1<br>
2-3. 단순 12월만 넘기는 조건이 아닌(40점 나옴) m이 12보다 작을때까지 반복해야함
3. 비교는 도합 정수 비교


