# Week 03

## 문제 리스트

|                |문제번호|난이도|문제제목|혼자 풀었나요?|
|----------------|-------|------|-------|-------------|
|4/19(수)|2562|하(중)|최댓값|O|
|4/19(수)|8958|하(중)|OX퀴즈|O|
|4/19(수)|4344|하(중)|평균은 넘겠지|O|
|4/19(수)|2577|하(중)|숫자의 개수|O|
|4/19(수)|15596|하(중)|정수 N개의 합|O|
|4/19(수)|11654|하(하)|아스키 코드|O|
|4/19(수)|2675|하(중)|문자열 반복|O|
|4/19(수)|1152|하(중)|단어의 개수|O|
|4/19(수)|2908|하(중)|상수|O|
|4/23(일)|9020|중|골드바흐의 추측|X|
|4/23(일)|1914|하(상)|하노이의 탑|O|

## 문법, 알고리즘 정리

### 2562 최댓값
파이썬 내장함수를 최대한 이용
max(), index()

### 4344 평균은 넘겠지
소수점 아래 몇 자리, 퍼센트로 나타내고 싶을 때
```
print(f'{count/c:.3%}')
```

### 9020 골든바흐의 추측
에라토스테네스의 해<br>
: 모든 소수에 대해 자신의 배수를 지워나간다.<br>
: 2부터 루트 N까지만 검색하면 된다.<br>
: 여기서 N은 4 <= N <= 10000<br>