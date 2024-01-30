# Week 01

## 문제 리스트

|          | 난이도  | 문제제목      | 혼자 풀었나요? |
|----------|------|-----------|----------|
| 01/30(화) | Lv01 | 정수 제곱근 판별 | O        |
| 01/30(화) | Lv01 | 문자열 나누기   | O        |
| 01/30(화) | Lv02 | N개의 최소공배수  | O        |





## 각 문제풀이별 생각정리
### 1. 정수 제곱근 판별
0. 1부터 시작해서 sq(n//2)까지 제곱이 n이 되는지 확인
1. 18번 테케에서 걸렸는데 1일때 처리를 제대로 안함

### 2. 문자열 나누기
0. 첫문자 Count 첫문자 아닌 Count
1. Count가 동일할시 해당 문자 인덱스 이후로 s를 자름
2. 종료조건은 s의 length가 0이거나 1 또는 문자열을 자르지 못하고 반복문을 종료했을때 (flag로 check)


### 3. N개의 최소공배수
0. 배열의 가장 큰 값의 배수가 최소공배수일거라 생각
1. 오름차순으로 정렬 후 마지막(max)값 제외함
2. Max값의 배수를 계산하면서 배열 값들과의 나머지 값이 0일때 끗