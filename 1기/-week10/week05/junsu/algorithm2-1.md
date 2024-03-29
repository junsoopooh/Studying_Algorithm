# 2.1 삽입정렬



**정렬문제**

**입력** : n개 수들의 수열 
$$
<a_1, a_2, …, a_n>
$$
 출력 :
$$
a’_1 <= a’_2 <= … <= a’_n
$$
을 만족하는 입력 수열의 순열(재배치) 

$$
<a’_1,a’_2, …, a’_n>
$$
 정렬하고자 하는 숫자를 **키**라고 한다.

 **의사코드**와 “실제” 프로그램 코드의 차이는, **의사 코드**에서는 알고리즘을 가장 분명하고 간결하게 서술할 수 있다면 어떤 표현 방법을 사용해도 좋음. 영어, 한글 문장등이 들어갈 수 도 있음. 데이터 추상화, 모듈화, 오류처리 등의 소프트웨어 공학 관점의 문제를 고려하지 않음.

 

**삽입정렬** : 카드 놀이를 할 때 손에 쥔 카드를 정렬하는 것. 무작위로 있던 책상 위에서 하나를 꺼내 왼손 위에 이미 든 카드와 오른쪽에서 왼쪽 방향으로 차례로 비교. 입력된 원소를 **적절한 위치로 정렬**

insertion-Sort(A)

```c
for j = 2 to A.length
	key == A[j]
    // A[j]를 정렬된 배열 A[1..j-1]에 삽입한다.
    I = j-1     
    while i > 0 그리고 A[i] > key
    A[i+1] = A[i]
    i = i-1
    A[i+1] = key
```

 

## 루프 불변성(Loop Invariant)과 삽입 정렬의 타당성

 인덱스 j는 왼손으로 가져가 정렬할 “현재 카드” 를 나타낸다. **for** 루프에서 인덱스 j로 표시되는 반복이 시작될 때 부분 배열 A[1, .., j-1]은 현재 손에 쥔 정렬된 카드이다. 부분 배열 A[ j + 1, .., n]은 아직 탁자에 쌓여 있는 카드다. 즉, A[1, .., j -1 ]은 처음에 탁자에 쌓인 순서대로 맨 앞부터 j -1번째까지의 값이지만 이제는 정렬되어 저장된 것.

 이를 **루프의 불변성**(Loop invariant)이라 함.



> 1~8행의 부분 배열 A[1 .. j-1]은 원래 A[1.. j-1] 원소지만 **for** 루프가 반복을 시작할 때 마다 정렬된 순서로 구성

 

루프 불변성의 세가지 특성

 

**초기조건** : 루프가 첫 번째 반복을 시작하기 전에 루프 불변성이 참이어야 한다.



**유지조건** : 루프의 반복이 시작되기 전에 루프 불변성이 참이었다면 다음 반복이 시작되기 전까지도 계속 참이어야 한다.



 **종료조건** : 루프가 종료될 때 그 불변식이 알고리즘의 타당성을 보이는 데 도움이 될 유용한 특성을 가져야 한다.

 

초기조건, 유지조건을 만족한다 => 루프가 반복을 시작할 때 루프 불변성은 항상 참

 수학적 귀납법과 유사하다.



1.  베이스 케이스: 첫 반복이 시작되기 전에 불변식이 만족함을 보이는 것 => 초기조건
2.  귀납적 단계 : 다음 반복으로 넘어갈 때 불변식이 만족함을 보이는 것 => 유지 조건

 

세 번째 특성이 가장 중요 => 루프 불변성을 보이는 목적이 알고리즘의 타당성을 보이는 것이기 때문! 

일반적인 수학적 귀납법과 달리 루프가 종료될 때 귀납적 과정도 끝남.



### ex) 삽입 정렬 알고리즘

 

**초기 조건** : 루프의 첫 반복이 시작되기 전, 즉 j = 2일 때 루프 불변성이 성립하는지 살펴본다.[^1] 

[^1]: 루프가 for일 경우, 초기조건 조사 시점은 루프의 카운트 변수가 초기화된 직후 루프 헤더에서 첫 검사하기 직전. 위에선 변수 j에 2가 할당된 직후, 즉 j <= length[A]인지를 처음 검사하기 직전.

이때 부분 배열 A[1..j-1]은 A[1] 한 개의 원소로 구성되는데, 원래는 A[1]의 값이다. 게다가 그 부분 배열은 정렬되어 있으므로 루프의 첫 반복 시작 전에 루프 불변성이  성립한다.

 **유지 조건** : 다음으로 두 번째 특성, 즉 매 반복 시 루프 불변성이 유지되는지를 살펴본다. 간단하게 설명하면 for 루프의 바디 부분은 A[j]의 올바른 위치를 찾을 때까지 A[j-1],A[j-2],A[j-3], … 을 오른쪽으로 한 자리씩 이동시키는 작업을 한 뒤(4~7행), A[j]값을 적절한 위치에 삽입한다(8행). 그러면 배열 A[1..j]는 기존 배열 A[1..j]와 동일한 원소를 정렬한 상태로 갖게 된다. j가 1씩 증가하면서 **for** 루프의 다음 반복에서 루프 불변성이 유지된다.

(정확히는, 5-7행의 **while** 루프에 대한 루프 불변성도 증명해야 함)

 

종료조건 : 루프가 종료되었을 때 상황을 조사해본다. 삽입 정렬의 경우 **for** 루프는 j가 A.length = n보다 커질 때, 즉 j가 1씩 증가하므로 j = n+1일 때 종료된다. 앞의 루프 불변성의 기술에서 j에 n+1을 넣어보면 부분 배열 A[1..n]은 원래 A[1..n]의 원소로 구성되지만 정렬된 순서로 저장됨. A[1..n]이 전체 배열이므로 배열 전체가 정렬되었으며 이는 알고리즘이 타당함을 의미.



## 루프 변성(loop variant)과 루프 불변성(loop invariant)

루프 불변성 : 각 루프의 반복 전후에 참이라는 조건이다. 루프의 각 반복이 '참'인 것이 루프의 실행 이후에도 바뀌지 않는다. 루프 불변성은 보통 알고리즘이 올바르게 작동하는 지를 증명하기 위해 사용된다.

루프 변성 : 루프가 종결되는 특정 값에 도달하기 전 까지 루프의 각 반복으로 증가하거나 감소하는 값이다. 루프 변성은 루프가 결국 종결되고 알고리즘이 무한 루프에 빠지지 않음을 보이기 위해 사용된다.

ex) 배열에서 특정 값을 탐색하는 알고리즘을 가정하자. 알고리즘은 값을 찾기 전까지 배열을 배회하는 루프를 사용한다.

- 루프 불변성 : 우리가 찾고 있는 값은 배열에서 아직 발견되지 않았다.
- 루프 변성 : 알고리즘이 최근에 본 배열의 index. 이 index는 배열의 끝에 도달하거나 값이 발견되기 전 까지 루프의 각 반복마다 1씩 증가한다.

위의 루프 불변성 사용하여 알고리즘이 올바르게 작동함을 증명할 수 있다.

- 초기 조건 : 첫 번째 반복 이전에 아직 발견 못했으므로 참
- 유지 조건 : 다음 반복이 시작되기 전에도 발견 못했으므로 참
- 종료 조건 : 알고리즘이 우리가 찾는 값을 찾아내어 루프가 종료되었음. 위 식은 타당성을 보이는데 도움이 되었음.

 

### 의사코드의 규칙(이 책)



-  들여쓰기는 블록 구조를 나타냄(반복문, 조건문 등)
-  for문 빠져나와도 루프 카운터 값 유지
- C++, 자바, 파스칼의 for문 : 루프 카운트 변수의 값 = 정의되지 않은 값 => for 루프를 처음으로 빠져나올 때의 값
- // : 주석
- i = j = e 는 i,j에 e 할당. j = e 후 i = j 한것과 같음
- 명시하지 않은 변수는 속하는 함수의 지역 변수. 전역변수는 명시
- A[i]는 A의 i번째 값. 0부터 아님
- ".."은 연속적인 부분
- 복합 데이터는 객체 형태, 객체는 필드로 구성. 특정 필드의 값은 {객체 이름}.{필드 이름}(ex. A.length)

 배열과 같은 객체를 나타내는 변수는 그 내용을 담고 있는 데이터에 대한 포인터로 다루어짐

- ex. y = x 실행되면 객체 x의 모든 필드 f에 대해 y.f값이 x.f 값과 같아진다. 즉, x와 y는 동일한 객체 가리킨다.

- 포인터가 아무 객체도 가리키지 않으면 NIL 이라는 특수값
- 프로시저(Procedure)의 매개변수들은 값에 의해 전달(call by value). 피호출 프로시저는 매개변수에 대해 복사본을 가지며, 피호출 프로시저에서 매개변수에 어떤 값을 할당하더라도 호출 프로시저에서 값의 변화를 모른다. 객체가 전달되면 객체의 데이터를 가리키는 포인터는 복사되지만 그 객체의 필드는 복사되지 않는다. (예: x가 피호출 프로시저의 매개변수 일 때 피호출 프로시저에서 x = y를 할당하는 것을 호출 프로시저에서는 확인할 수 없다. 그러나 x.f = 3과 같은 할당문은 호출 프로시저에서도 변화를 알 수 있다.) 
- 이와 비슷하게 배열을 함수의 매개변수로 쓸 때는 배열 전체를 넘기지 않고 배열의 포인터만 넘긴다. 이 경우에도 배열의 원소값을 변화시키면 호출 프로시저에서 확인 할 수 있다.
- return문은 호출되는 즉시 호출 프로시저로 돌아간다. 대부분의 return문은 값을 호출 프로시저로 보낸다. 이 책의 의사코드에서는 많은 프로그래밍 언어들과 달리 하나의 return문으로 여러 값을 리턴할 수 있다.
- ‘and’와 ‘or’ 같은 이진 논리 연산자는 조기 차단할 수 있다. 즉, “x and y”문에서 x를 먼저 계산한다. x가 false면 식의 결과가 True가 될 수없으므로 y를 계산조차 하지 않는다. 반면, x가 true면 식의 결과를 계산하기 위해 y값도 반드시 계산해야 한다. 비슷하게 ”x or y”식에서 x의 결과값이 false일 경우에만 y를 계산한다. 이렇게 조기 차단되는 연산자를 사용하면 “x =/ NIL and x.f = y”와 같은 이진 논리 식에서 x가 NIL인 경우 x.f를 계산할 때 어떤 상황이 벌어질지 걱정하지 않고 사용할 수 있다.
- error는 프로시저가 호출되는 동안 조건이 잘못되어 오류가 발생함을 의미한다. 발생한 오류에 대한 처리는 호출 프로시저에서 이루어지므로 프로시저에서는 오류 처리를 명시하지 않는다.

------



## 연습문제

### 2.1-1

그림 2.2를 모델로 이용해 수열 A = <31,41,59,26,41,58>이 입력으로 주어질 때 INSERTION-SORT의 동작을 설명하라.

![figure2-2.png](https://github.com/junsoopooh/Studying_Algorithm/blob/week05/junsu/week05/junsu/figure2-2.png)



#### 나의 답

- <31,41,59,26,41,58>
- 31이 삽입된다. <31>
- 41이 삽입된다. <31,41>
- 41을 31과 비교한다. <31,41>
- 41이 더 크기 때문에 위치를 변경하지 않는다. <31,41>
- 59를 삽입한다. <31,41,59>
- 59를 41과 비교한다. <31,41,59>
- 59가 더 크기 때문에 위치를 변경하지 않는다. <31,41,59>
- 26을 삽입한다. <31,41,59,26>
- 26을 59와 비교한다. <31,41,59,26>
- 26이 더 작기 때문에 59와 위치를 바꾸고 비교 대상을 41로 교체한다. <31,41,26,59>
- 26이 더 작기 때문에 41과 위치를 바꾸고 비교 대상을 31로 교체한다. <31,26,41,59>
- 26이 더 작기 때문에 31과 위치를 바꾼다. <26,31,41,59>
- 41을 삽입한다. <26,31,41,59,41>
- 41을 59와 비교한다. <26,31,41,59,41>
- 41이 더 작기 때문에 59와 위치를 바꾸고 비교 대상을 41로 교체한다. <26,31,41,41,59>
- 비교하는 두 수의 크기가 같기 때문에 위치를 변경하지 않는다. <26,31,41,41,59>
- 58을 삽입한다. <26,31,41,41,59,58>
- 58을 59와 비교한다. <26,31,41,41,59,58>
- 58이 더 작기 때문에 59와 위치를 바꾸고 비교 대상을 41로 교체한다. <26,31,41,41,58,59>
- 58이 더 크기 때문에 위치를 변경하지 않는다. <26,31,41,41,58,59>
- 정렬 완료 : <26,31,41,41,58,59>



### 2.1-2

수열을 오름차순 대신 내림차순으로 정렬하도록 INSERTION-SORT 프로시저를 재작성하라.



#### 나의 답

INSERTION-SORT(A) 오름차순

```c
for j = 2 to A.length
    key = A[j]
    // A[j]를 정렬된 배열 A[1 .. j-1]에 삽입한다.
    i = j - 1
    while i > 0 그리고 A[i] > key
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key
```

INSERTION-SORT(B) 내림차순

```c
for j = 2 to B.length
    key = B[j]
    // B[j]를 정렬된 배열 B[1 .. j-1]에 삽입한다.
    i = j - 1
    while i > 0 그리고 B[i] < key
        B[i+1] = B[i]
        i = i - 1
    B[i+1] = key
```



### 2.1-3

다음의 **검색 문제**를 생각해보자.

**입력**: n개 수들의 수열 A와 어떤 값 v
$$
A=<a_1,a_2,...,a_n>
$$
**출력** v = A[i]를 만족하는 인덱스 i. v가 배열 A에 존재하지 않으면 특수값 NIL



수열을 읽어 보고 v값을 찾아보는 **선형 검색** 의사코드를 작성하고, 루프 불변성을 이용해 그 알고리즘이 타당함을 증명하라. 루프 불변성의 세 가지 특성을 만족하는지 반드시 확인해야 한다.



#### 나의 답

LINEAR-SEARCH(A)

```c
for i = 1 to A.length
    if A[i] == v
        print(i)
        break
print(NIL)
```

루프 불변성

초기 조건 : i에 1이 할당된 직후 i가 A.length보다 작음을 검사하기 직전, 우리가 찾는 v를 값으로 하는 원소를 배열 A에서 찾지 못했음(참)

유지 조건 : 매 반복 시 다음 반복 전 여전히 찾지 못했음이 참으로 유지되고 있음(참)

종료 조건 : 반복이 종료되면, 위 condition의 참 여부에 따라 위 알고리즘으로 원하는 인덱스 i를 찾았는 지 알 수 있음.

세가지 특성을 모두 만족한다.



### 2.1-4

원소가 n개인 두 배열 A, B에 저장된 두 개의 n비트 이진수를 더하는 문제를 고려해보자. 두 이진수의 합은 원소가 n+1개인 배열 C에 이진수 형태로 저장되어야 한다. 이 문제를 엄밀하게 서술하고 두 정수의 합을 구하는 의사코드를 작성하라.



#### 나의 답

이진수에서 각 자릿수가 가질수 있는 수는 0,1이다. 두 이진수의 같은 자릿수가 모두 최댓값인 1일 경우, 더하면 0이 되고 다음 자릿수에 1이 추가된다. 두 이진수의 다음 자릿수가 모두 1이라 하더라도 총 1+1+1이 되어 1만 남기고 다음 자릿수로 1을 넘기게 된다. 즉 이진수의 합에서 한 자릿수의 합은 그 다다음 자릿수에 영향을 끼칠 수 없다. 이는 사실 진법(위치적 기수법)과 상관없이 동일한 내용이다. n진법에서 숫자는 n-1까지 존재하는데, 한 자릿수에서 합의 최댓값은 2*(n-1)이다. 이 값은 2n을 넘을 수 없으므로 다음 자릿수에는 1이상의 값을 올릴 수 없다. 두 자릿수 뒤의 값에 영향을 끼치기 위해 필요한 수는 n^2다. n이 가장 작은 2진법의 경우, 두 수를 더할 때 한 자릿수에서의 합이 4가 되어야 다다음 자릿수에 영향을 끼칠 수 있는데 3이 최대의 값이다.  결국 어떤 경우에도 자릿수가 같은 두 수를 더해 나온 결과의 자릿수가 2 이상 증가할 수 없다. 

따라서 n비트 이진수 두개를 더해도 n+1비트 이진수보다 자릿수(비트)가 커질 수 없다.

```c
for i = 1 to n+1
    C[i] = 0

for i = 1 to n
    if (A[i] + B[i] + C[i])>= 2 // 이전 반복에서 이전 자릿수의 합으로 C의 원소가 1이 되어있을 수 있다.
        C[i] += (A[i] + B[i] + C[i])%2
        C[i+1] = 1
   	else
        C[i] = A[i] + B[i] + C[i]
```

 

