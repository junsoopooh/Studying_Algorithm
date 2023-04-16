|**문제**|시간복잡도|분류|
|:---:|:---:|---|
|9498 시험성적|O(1)|pass|
|2753 윤년|O(1)|pass|
|1085 직사각형에서의 탈출|O(1)|pass|
|2739 구구단|O(N)|pass|
|10950 A+B-3|O(N)|pass|
|2438 별찍기-1|O(N)|pass|
|10871 X보다 작은 수|O(N)|pass|
|2869 달팽이는 올라가고 싶다|O(1)|pass|
|1978 소수찾기|O(√N)|pass|

<br><br>

<details>
<summary>2753 윤년</summary>
<div markdown="1">       

😎알면 좋은 개념😎 <br>
    ~ 이면서 AND 논리연산자 <br>
    또는 OR 논리연산자 <br>

</div>
</details>

<details>
<summary>2869 달팽이는 올라가고 싶다.</summary>
<div markdown="1">       

😎식 세우기😎 <br>
    도달하는 날 : X일 <br>
    총 올라가는 횟수 : X번 <br>
    내려가는 횟수는 (X-1)번 <br>
    AX + B(X-1) = V <br>
    X = (V-B)//(A-B) <br>
    X값이 나머지가 있으면 7.5일이란 말이 이상하지 않나? 하루 더 걸리는 거니, +1 해줘야함. <br>

</div>
</details>

<details>
<summary>1978 소수찾기</summary>
<div markdown="1">       

😎알면 좋은 개념😎 <br>
    에라토스테네스의 체<br>
    ![image](https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif) <br>
    <br>
    1,2는 소수가 아님. <br>
    <br>
    2부터 √N 까지만 탐색하면 됨.<br>
    왜? <br>
    100 의 약수들을 나열해보면 <br>
    1, 2, 4, 5, 10, 20, 25, 50, 100 <br>
    사실상 10(√100)까지 범위내에서 100의 약수 모두 구할 수 있음<br>
    100/2 = 50, 100/4 =25 이므로~~<br>
    <br>
    2를 제외한 모든 2의 배수를 소수가 아닌 걸 표시!<br>
    √max(nums) 탐색 범위내에서 소수가 아닌 걸 낼 수 있다. <br>
</div>
</details>
