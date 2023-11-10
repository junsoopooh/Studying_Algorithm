# Week 01

## 문제 리스트

|          | 난이도  | 문제제목   |혼자 풀었나요?|
|----------|------|--------|-------------|
| 11/10(금) | Lv01 | 평균 구하기 |O|



## 각 문제풀이별 생각정리
### 평균 구하기
- 평균 구하는 모듈이나 라이브러리가 있지 않을까 ? 
- 그래서 찾아봄 -> 평균을 구하는 4가지 방법 정리
1. 흔히 아는 반복문으로 구하는 방법
2. 내가 문제에서 푼 **sum**과 **len**을 이용한 평균을 구하는 방법
3. 파이썬 **numpy** 모듈로 평균 구하기
> pip install numpy 모듈을 설치한 후 사용
```
import numpy

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 평균 구하기
average = numpy.mean(arr)

출처: https://blockdmask.tistory.com/559
```
4. statiscics 라이브러리 이용
> 해당 라이브러리는 여러 수학 관련 함수를 제공해줌
> 평균을 구하는 함수는 **mean**이라는 함수
```
import statistics

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [100, 90, 80, 10, 20, 30, 60, 70, 50, 40]

# 평균 구하기
result1 = statistics.mean(arr1)
result2 = statistics.mean(arr2)

출처: https://blockdmask.tistory.com/559 [개발자 지망생:티스토리]
```
