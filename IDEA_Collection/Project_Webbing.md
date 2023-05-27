# Project : Webbing

## 계획서 

링크 : https://github.com/junsoopooh/Studying_Algorithm/blob/main/IDEA_Collection/webbing/webbing.md

## 참고 링크

1. canva 사이트 : https://www.canva.com/ko_kr/graphs/ 
2. https://www.finereport.com/kr/%EA%B7%B8%EB%9E%98%ED%94%84-%EA%B7%B8%EB%A6%AC%EB%8A%94-%EC%82%AC%EC%9D%B4%ED%8A%B8-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-top10-%EB%AA%A8%EC%9D%8C-2021%EC%B5%9C%EC%8B%A0/

## 설명 요약

다양한 주제와 입력에 대해 간편하고 다양한 시각화 제공툴

## 선정 이유

단편화된 개념의 동기화를 제공하고 한 눈에 흐름을 파악하는데 도움을 주기 위함

## 핵심 기능

1. 특정 범위 내에서 개념간의 관계성을 알맞게 시각화

2. 다양하고 복잡한 코드의 함수 호출 Flow를 알맞게 시각화 + 각 point에서 variable 값 및 자료형 제공

3. 각 노드와 외부 자료(URL, 파일 등)의 연결

4. 유저의 수정을 돕는 보조 도구 제공
5. 다양한 시각화 형태, 유저의 다양한 입력에 대한 수용성(코드, 웹페이지, 텍스트, 그림)

## 기술 스택

- Front : React + typescript (이후 여건에 따라 모바일 어플 시도)
- Back : Django VS spring (동시성 및 멀티스레딩이 좋은 Java. 우린 Django 써도 되지 않을까? '빠르게' 개발하는데 적합하고, 편리함)
- DBMS : NoSQL(MongoDB?)
- 기타 : AWS?

## 약점

- 다양한 시각화 결과 필요
- 다양한 입력에 관한 반응성 필요
- 부족한 백엔드의 도전 과제

## 개선 방안

### 1. 다양한 시각화 결과

비슷한 기능의 사이트들을 ~~베끼자~~**벤치마킹**



### 2. 다양한 입력에 관한 반응성 

웹사이트가 아닌 로컬 프로그램으로 만든다. 서버 연결은... 사람들의 결과물 올리기? 

참고 링

https://dontdiethere.tistory.com/43

### 3. 백엔드의 추가적인 도전 과제 설정

#### (1) 동작 취소 기능

undo(rollback) 와 redo 기능인가보다

이전 상태를 저장하니 마니 좌표로 두니 마니 고민 흔적 보임

꽤 쉽지않은 도전으로 보임. 그래서 재밌겠음.

참고 링크

http://1st.gamecodi.com/board/zboard.php?id=GAMECODI_Talkdev&no=1089

https://brownbears.tistory.com/181

https://hengki.net/96



#### (2) 각종 동작 자동완성(기능 검색바 제공)

여러 자료들이 있다. 읽기 귀찮아서 일단 가능은 한것으로 판단.

참고 링크

https://velog.io/@jake93/django-%EA%B2%80%EC%83%89%EC%96%B4-%ED%95%84%ED%84%B0-%EA%B5%AC%ED%98%84

https://equus3144.medium.com/django%EB%A1%9C-%EA%B2%80%EC%83%89-%EA%B8%B0%EB%8A%A5-%EB%A7%8C%EB%93%A4-%EB%95%8C%EC%9D%98-%ED%95%B5%EC%8B%AC-orm-filter-567be01021c5

#### (3) 최근 수정 파일에 대한 클라우딩기능

서버에 연결해서 최근 3개정도 하면 될지 모르겠다. 진짜 하는 방법을 모르겠다.

#### (4) 자동저장

모르겠다. 5분? 10분?에 한번 자동저장 갈기도록 구현하는건 어떨까?

#### (5) 입력 데이터 자동 분석 

백엔드는 '데이터'를 다룬다. 저장, 전달, 가공 등등.. 데이터 처리에 대한 도전적인 기술을 추가해야 한다. 유저가 제공한 입력에서 핵심 키워드를 parsing 할 수 있다면? 이를 바탕으로 시각화 할수 있다면 좋을듯하다. 다양한 입력 방식 고려해보자.

- 마크다운 or WebPage : H1,H2 등을 추출?
- 단순 word : 제목처럼 따로 떨어져 있는 단어 추출? 반복적인 단어 추출?
- 코드 : 가장 상위 부모 함수 구별?
- 이미지 : 페이지에서 text를 읽어야 하나?
-  폴더 : 폴더 내 각 파일 제목을 통해 구성?

입력 확장자로 구분해야할까? 아니면 유저가 본인이 넣을것을 선택하도록 해야할까?



#### (6) 함수 flow 추적

기존 알고리즘 문제를 풀 때 VScode에서 디버깅을 하며 각 breakpoint에서 variable을 확인하였다. 이 기능을 구현할 순 없을까? VScode에선 뒤로는 못갔는데..

https://latte-is-horse.tistory.com/193 사이트 참조



