# Week 11

## 문제 리스트

|       |문제번호|난이도|문제제목|혼자 풀었나요?|
|-------|-------|------|-------|-------------|
|7/21(금)|10000|플래티넘4|원 영역|X|
|7/25(화)|6549|플래티넘5|히스토그램에서 가장 큰 직사각형|O|
|7/25(화)|18258|큐 2|실버 4|O|
|7/25(화)|2164|카드 2|실버 4|O|

## 문법, 알고리즘 정리

### 10000 원 영역
- 37번 라인, 또 다른 계산을 위해 원을 추가해주어야 한다는 것을 이해하기까지가 오래걸림

### 6549 히스토그램에서 가장 큰 직사각형
- 높이가 0이 올 수도 있다는 걸 파악했어야 했음
- 스택에 남아있는 애들도 확인해주어야 했음, 그래서 세로로 확인 1번, 가로로 확인 1번씩 해줌

### 18258 큐 2
- 그냥 리스트를 이용하면 시간 초과
- deque를 이용해서 시간 초과 해결

### 2164 카드 2
- 카드 밑으로 내릴 때, popleft하고 append하는 방법 말곤 없나?