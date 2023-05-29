리트코드 사용법

1. 리트코드 접속 (https://leetcode.com/)

![leet1](Leetcode/Leetimg/leet1.png)

2. 왼쪽 위 Explore 누르고 Get Started 클릭

![leet2](Leetcode/Leetimg/leet2.png)

2. 오른쪽 위 Sign up 으로 회원가입(원하지 않으면 9번으로 SKIP)

![leet3](Leetcode/Leetimg/leet3.png)

2. 아래 구글,깃허브, 페이스북 중 가운데 깃허브 아이콘 클릭(깃허브 아이디와 연동)

![leet4](Leetcode/Leetimg/leet4.png)

2. 혹은 그냥 ID, 비밀번호, 비밀번호 확인, e-mail 주소 입력 해도 됨.
3. Proffessional -> 경력 햇수 -> 경력 포지션 선택 -> Next

![leet5](Leetcode/Leetimg/leet5.png)

![leet6](Leetcode/Leetimg/leet6.png)



2. 취업 희망 포지션 선택(없으면 밑에 박스만 체크) -> 최근에 본 취업 면접

![leet7](Leetcode/Leetimg/leet7.png)

![leet8](Leetcode/Leetimg/leet8.png)

2. 다음은 신규 가입자를 위한 쉬운 알고리즘 문제들이 나오는데 풀어봐도 되고 안 풀어 봐도 됨

![leet9](Leetcode/Leetimg/leet9.png)

2. 상단에 problems 클릭

![leet10](Leetcode/Leetimg/leet10.png)

2. All Topics 옆에 Algorithms를 클릭한 후 밑 Tags 클릭
3. ![leet11](Leetcode/Leetimg/leet11.png)
4. 원하는 Topic 검색하거나 expand하여 선택(DFS, Binary Search, Dynamic Programming 등)

![leet12](Leetcode/Leetimg/leet12.png)

2. 옆에서 Difficulty(난이도) 도 조절 가능

![leet13](Leetcode/Leetimg/leet13.png)

2. 새롭게 뜬 목록에서 문제 번호, 정답률, 난이도 클릭하여 정렬 가능

![leet14](Leetcode/Leetimg/leet14.png)

2. 268번 Missing Number 문제를 검색하여 같이 풀어보자.

![leet15](Leetcode/Leetimg/leet15.png)



예시 : 268번 Missing Number 문제

1. 다음과 같은 화면을 볼 수 있음.

![leet16](Leetcode/Leetimg/leet16.png)

1. 왼쪽은 문제 내용과 예시.
2. 백준과 달리 Input값 정의, 받는 코드 필요 없고 print로 출력도 필요 없음.
3. 아래 예시는 입력값과 그 결과, 그 결과가 나오게 된 방식 설명이 쓰여있음.
4. 밑에는 범위, 가장 밑에 Related Topics 눌러서 관련 개념 확인할 수 있음.

![leet17](Leetcode/Leetimg/leet17.png)

1. 오른쪽은 정답 제출 페이지
2. 왼쪽 위에서 언어 선택 가능

1. ![leet18](Leetcode/Leetimg/leet18.png)오른쪽 위에 timer가 있고 그 밑 5개 중 가운데를 누르면 맨 처음 초기 상태로 돌아감
2. 아래의 Run을 누르면 example을 입력하여 나온 결과를 알 수 있음.
3. Submit으로 제출

![leet19](Leetcode/Leetimg/leet19.png)

1. 왼쪽 페이지 위에서 Submission을 누르면 제출 이력을 알 수 있음.

![leet20](Leetcode/Leetimg/leet20.png)

1. 정답을 제출하면 초록색 Accepted가 있는데 누르면 다른 제출들에 비해 메모리 사용과 작동 시간이 어떤지 알 수있음.
2. 뜨는 숫자는 내 결과이고, %는 하위 백분율을 나타냄. 그래프에서 오른쪽으로 갈 수록 하위권임. 13%면 하위 13%이므로 100명중 87등 이란 뜻임

![leet21](Leetcode/Leetimg/leet21.png)

문제 : 0부터 n의 범위 내에서 n개의 서로 다른 정수를 포함하는 배열 `nums` 가 있을 때, 배열에 없는 유일한 숫자 하나를 찾아 반환하라. 

예시 1

nums = [3,0,1]

nums의 원소 갯수에 따라 n = 3이므로 0부터 3까지 중 `nums`에 없는 정수 찾아서 반환

답 : 2

예시 2

nums = [0,1]

nums의 원소 갯수에 따라 n = 2이므로 0부터 2까지 중 `nums`에 없는 정수 찾아서 반환

답 : 2





정답 코드

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
```



Leetcode에 좋은 문제가 많다고 하니 도움이 되길 바라며, 추가적으로 궁금하면 언제든지 물어보길 바람.

