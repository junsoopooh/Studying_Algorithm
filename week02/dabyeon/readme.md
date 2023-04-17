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
|겹치는 선분의 길이|O(N²)|pass|
|OX퀴즈|O(N)|pass|
|안전지대|O(N²)|pass|

<br><br>

<details>
<summary>2753 윤년</summary>
<div markdown="1">       

😎알면 좋은 개념😎 <br><br>
    ~ 이면서 AND 논리연산자 <br>
    또는 OR 논리연산자 <br>

</div>
</details>

<details>
<summary>2869 달팽이는 올라가고 싶다.</summary>
<div markdown="1">       

😎식 세우기😎 <br><br>
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
    에라토스테네스의 체<br><br>
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

<details>
<summary>OX 퀴즈</summary>
<div markdown="1">       

😎알면 좋은 개념😎 <br>
    eval()함수<br><br>
    실행할 코드를 string형태로 전달 <br>
    코드 내부적으로 딕셔너리 mapping을 해 <br>
    integer 형태로 값을 return <br>
    예를 들어 eval("7+3") 은 integer type의 10을 반환 <br>
</div>
</details>

<details>
<summary>안전지대</summary>
<div markdown="1">       

😎알면 좋은 개념😎 <br>
    2차원 배열 index 범위<br><br>
    만약 5행 3열 2차원 배열을 생성했다고 가정하자!<br>
    상하좌우 대각선 영역에 지뢰를 설치하고 싶다면,<br>
    index범위를 벗어나지 않는 영영에서 지뢰를 설치해야 한다.<br><br>
    내장함수 min(), max()를 활용해 범위를 설정하면 편하다. <br>
    row의 경우 index범위가 0~4까지 <br>
    지뢰 설치되는 row의 범위 : max(0, cur_row-1) ~ min(4, cur_row+1) <br>
    column의 경우 index범위가 0~2까지 <br>
    지뢰 설치되는 rol의 범위 : max(0, cur_rol-1) ~ min(4, cur_rol+1) <br>
</div>
</details>
