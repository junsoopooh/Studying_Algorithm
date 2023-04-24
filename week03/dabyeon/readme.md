|**문제**|시간복잡도|분류|
|:---:|:---:|---|
|2562 최댓값|O(N)|pass|
|8958 OX퀴즈|O(N)|pass|
|4344 평균은 넘겠지|O(N)|pass|
|4577 숫자의 개수|O(N)|pass|
|15596 정수N개의 합|O(1)|pass|
|11654 아스키코드|O(1)|pass|
|2675 문자열반복|O(N)|pass|
|1152 단어의 개수|O(1)|pass|
|2908 상수|O(1)|pass|
|9020 골드바흐의 추측|O(N)|pass|
|1914 하노이의 탑|O(2ⁿ)|accepted|
|프로그래머스, 평행|O(1)|pass|
|프로그래머스, 문자열 내 마음대로 정렬하기|O(1)|pass|
|프로그래머스, [1차] 비밀지도|O(N)|pass|


<br><br>

<details>
<summary>8958 OX퀴즈</summary>
<div markdown="1">       

😎등차수열 합😎 <br><br>
    첫항 s, 마지막항 e, 항의 갯수 n <br>
    ((s+e)*n)/2 <br>

</div>
</details>

<details>
<summary>4344 평균은 넘겠지</summary>
<div markdown="1">       

😎소수점 자리수 표현😎 <br><br>
    round(40.00000, 3) → 40.0 <br>
    '{:.3f}'.format(40.00000) → 40.000 <br>

</div>
</details>

<details>
<summary>11654 아스키코드</summary>
<div markdown="1">       

😎아스키코드 내장함수😎 <br><br>
    ord("A") → 97 <br>
    chr(97) → "A" <br>

</div>
</details>

<details>
<summary>2908 상수</summary>
<div markdown="1">       

😎문자열 뒤집기😎 <br><br>
    string = "Hello!" <br>
    string[::-1] <br>
    "".join(reversed(string)) <br>
</div>
</details>

<details>
<summary>1914 하노이의 탑</summary>
<div markdown="1">       

😎n개 디스크 옮기기😎 <br><br>
    2ⁿ-1 <br>
    <br>
    수학적 귀납법 증명 <br>
    2^(n-1)-1 ((n-1)개 디스크 이동) + 1(가장 큰 디스크 이동) + 2^(n-1)-1 ((n-1)개 디스크 이동) <br>
    2*2^(n-1)-1 = 2ⁿ-1
</div>
</details>

<details>
<summary>프로그래머스, 문자열 내 마음대로 정렬하기</summary>
<div markdown="1">       

😎정렬 기준 lamda😎 <br><br>
    strings.sort(key = lambda x:x[n]) <br>
</div>
</details>

<details>
<summary>프로그래머스, [1차] 비밀지도</summary>
<div markdown="1">       

😎10진수를 2진수로 변환😎 <br><br>
    bin(31) → 11111 <br><br>

😎문자열 0으로 채우기 zfill😎 <br><br>
'38'.zfill(5) → '00038'<br>
'38'.rjust(5, '0') → '00038'<br>
</div>
</details>