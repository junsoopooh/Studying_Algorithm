|**문제**|시간복잡도|분류|
|:---:|:---:|---|
|1181 단어정렬|O(1)|pass|
|2309 일곱난쟁이|O(N)|pass|
|2789 블랙잭|O(N)|pass|
|9663 N_Queen|O(N!)|accepted|
|1074 Z|O(NlogN)|pass|
|프로그래머스, 없는 숫자 더하기|O(1)|pass|
|프로그래머스, x만큼 간격이 있는 n개의 숫자|O(N)|accepted|
|프로그래머스, 하샤드 수|O(N)|pass|

<br><br>

<details>
<summary>1181 단어정렬</summary>
<div markdown="1">       

😎정렬 기준😎 <br><br>
    
list.sort(key = lambda x : 기준) <br>

</div>
</details>

<details>
<summary>9663 N_Queen</summary>
<div markdown="1">       

😎Backtracking😎 <br><br>
    
탐색 경로를 최소한으로 줄이는 방법으로 <br>
솔루션을 찾으면 재귀가 중지되고 함수가 반환! <br>
함수가 반환되면 호출 스택이 해제되고 알고리즘이 이전 수준의 재귀로 역추적!! <br>

</div>
</details>

<details>
<summary>프로그래머스, x만큼 간격이 있는 n개의 숫자</summary>
<div markdown="1">       

😎range(a1, a2, a3) 인자 에러😎 <br><br>
    
for i in range(x, y, x): <br>
ValueError: range() arg 3 must not be zero <br>
세번째 인자로 0이 들어가면 오류 발생!<br>
step size cannot be zero!!!<br>
세번째 인자 생략하는 for i in range(x,y) 이런식으로 사용하는거 추천...<br>

</div>
</details>