# 나만의 무기 프로젝트

## 관련 개념

### 프로젝트 범위

- PoC(Proof of Concept, 개념 증명) 

    - 의미 : 도입하기 전에 이를 검증하기 위해 사용. 실체화하여 타당성을 증명

    - 의의 : 신기술 or 신제품이 도입 목적에 부합되는지 검증
    - 검증 : 생각한대로 동작하는가? 도입 가능한가?
    - 실사용자인 고객의 사용/피드백 X

- Prototype(프로토타입)

    - 의미 : 정보시스템의 미완성 버전 또는 중요한 기능들이 포함되어 있는 시스템의 초기모델

    - 의의 : 중요한 기능들이 포함된 초기모델(SW 개발 착수전 검증/승인)
    - 검증 : 설계대로 개발/양산 가능한가?
    - 실사용자인 고객의 사용/피드백 없을 수도 있음

- Pilot(시범 적용)

    - 의미 : 소규모로 테스트해서 추후 발생할 수 있는 여러 문제의 원인을 미리 파악하고 수정 보완하기 위해 모의로 시행해 보는 활동

    - 의의 : 새로운 정책 or 서비스 확산의 첫 번째 시범 적용
    - 검증 : 더 넓은 그룹으로 확장 가능한가?
    - 실사용자인 고객의 사용/피드백 O. 지속적인 검증/사용이 아닌 성공/실패 확인

- <u>**MVP**(Menimum Viable Product, 최소 실행가능 제품) : 고객에게 가치 제공. 고객의 피드백을 받아 생존하기 위한 최소한의 노력을 들여 만든 기능 구현한 제품.</u>

------



## 기술 스택

### Front

1. React(ReactNative)
    - 대중적(방대한 생태계), 컴포넌트에 집중된 라이브러리, 높은 자유
    - SSR(Server Side Rendering) 지원
    - React Native로 모바일등의 타 환경 개발
    - Independent Componenets : 한 페이지 내에서 여러 부분(버튼, 표 등)이 독립된 컴포넌트. 복잡한 코드의 유지, 보수에 용이
    - One-way data flow : 규모가 큰 데이터의 흐름 추적 용이. 데이터 흐름의 변화 예측 가능. 복잡해지는 코드는 VDOM으로 해결
    - VDOM(Virtual Documnet Object Model) : 코드 내에 원하는 위치에 접근하는 방식을 DOM이라 함. 객체의 변화 감지하면 DOM을 다시 그리지 않고, 가상의 DOM을 만들어 전체가 아닌 해당 부분만 실제 DOM에 반영하여 브라우저 리소스를 최소화하고 효율성과 속도를 높임.
    - HTTP 클라이언트, 라우터, 심화적 상태 관리등의 기능 내장 X, 공식 라이브러리 X
    - ReactNative : 모바일, JS언어 사용
2. Flutter
    - 구글에서 개발, 관리하는 오픈소스
    - 동일 언어로 다양한 플랫폼 개발(ios, web, linux, macOS, android, Windows)
    - 많은 레퍼런스
    - 다양한 Editor(Android Studio, IntelliJ, VS code) 사용 가능
    - 직접 컴파일되어 Render하여 빠른 성능
    - 양질의 DX(developer experiment) 제공
    - 아직 부족한 생태계
    - 잦은 업데이트
    - 단 : Dart 언어 학습 필요(Learning Curve)
3. Vue
    - 쉬운 사용법
    - 모듈 번들러(ex. Webpack) 사용하지 않고, CDN에 있는 파일을 로딩 하는 형태로 스크립트를 불러옴.
    - HTML을 템플릿처럼 그대로 사용할 수 있어서 마크업을 만들어주면 작업 흐름이 매끄러워 짐.
    - 공식 라우터, 상태관리 라이브러리 존재
    - VDOM 사용
4. Typescript
    - 대중적
    - 정적 타입의 컴파일 언어여서 코드 작성 단계에서 타입을 체크해 오류 확인 가능함
    - 미리 타입을 결정하여 빠른 실행 속도, 전달되는 데이터 유형이 파악되어 오류 찾기 쉬움
    - 타입 결정으로 인한 코드량 증가, 긴 컴파일 시간
    - 객체 지향 프로그래밍 지원
    - 높은 수준의 코드 탐색과 디버깅
    - 자바스크립트 호환
    - 강력한 생태계
    - 점진적 전환 가능
    - 단 : 새로운 언어에 대한 러닝 커브(Learning Curve)
    - 단 : 낮은 가독성과 많은 코드량
    - 리액트, 뷰, 앵귤러와 호환
5. Angular
    - 특정 기능 구현시 편리함
    - 라우터, HTTP 클라이언트 등 웹 프로젝트에서 필요한 대부분의 도구들 내장
    - 주로 타입스크립트와 사용

6. Next.js

- CSR(Client Side Rendering) 방식으로 동작
- 개발환경/코드분할/파일 기반 구조 등 다양한 기능 제공
    - 다이나믹 라우트
    - SSR
    - 파일을 하나로도, 쪼갤수도 있음. 알아서 쪼개줌
- SEO 검색 엔진 최적화
- 간단한 API 구성 가능
- Velcel을 통한 손쉬운 배포



7. Swift(ios)

8. Kotlin(Android)

### Back

1. Python Flask
    - 가볍고 단순한 특징
    - ORM 기능 부재로 양식 처리, 인증, 보안, DB 연결 등 직접 해야함

2. Django
    - 스크립트 언어로 간결하고 쉬움
    - 다양한 운영체제 활용도
    - 강력하고 많은 라이브러리
    - 파이썬 라이브러리 사용 가능
    - 빅데이터 및 클라우드, AI에서 많이 쓰

3. Java Spring(Boot)
    - 상대적으로 단순한 작성 코드
    - 정부에서 오픈소스 제공
    - POJO(Plain Old Java Object, 순수 Java만을 통해서 생성한 객체) 프로그래밍 지향
    - IoC/DI(Inversion of Control / Dependency injection) 
    - AOP(ASpect oriented programming)
    - PSA(Portable Service Abstraction)
    - 스프링 개발시 복잡한 설정의 단순화 => 스프링부트

4. Node.js
    - 빈번하고 많 I/O처리에서 우수한 성능
    - 서버 확장의 용이성
    - JS언어로 백엔드 까지 작성가능

5. Go
    - 컴파일 언어지만 컴파일러의 컴파일 속도가 빨라 인터프리티 언어처럼 쓸 수 있음.
    - 쉬운 접근, 간결한 코드, 높은 성능
    - 자료형의 정적 타입 검사
    - 풍부한 라이브러리
    - 단순함과 실용성
    - 단 : 다중 플랫폼 지원 힘듬
    - 단 : 고성능 연산에선 C보다 느리고 저수준에선 무거운 런타임
    - 단 : 언어 차원의 버그 방지 부 



### DBMS

- SQL VS NoSQL
    - SQL
        - Structed Query Language
        - DB 시스템에서 자료를 처리하는 용도로 사용되는 구조적 데이터 질의 언어
    - NoSQL
        - 대부분 목적이 클러스터에서 실행이라 관계형 모델 사용 X
        - 대부분 오픈 소스
        - 일관성보다 다수의 읽고 쓰는 상황에서 성능 우선시
        - 분산 저장
        - 데이터 구조 상관 X, ORM 프레임워크 필요 X

1. MongoDB
    - NoSQL
    - 크로스 플랫폼 도큐먼트 지향 데이터베이스
    - JSON 형태의 동적 스키마형 문서(BSON)
    - 같은 조건에서 기존 RDBMS보다 월등한 속도
    - 일관성 없는 데이터에선 좋지만 일관성 필요하면 사용 힘듬
2. MySQL
    - SQL

### 

### 서버

1. AWS : Amazon
2. Azure : Microsoft

------



## 아이디어 후보 

### Middle Map

- 계획서 : https://github.com/junsoopooh/Studying_Algorithm/blob/main/IDEA_Collection/Middle_Map/Middle_Map.md

- 설명 요약 : 다양한 플랫폼에서 최소한의 필터링을 거친 데이터의 요약 전달 및 시각화. 실사용자의 유의미한 데이터 수집

- 선정 이유 : 유저가 많은 출처에서 온 데이터를 편리하게 얻어 결정에 도움을 주기 위함

- 핵심 기능
    - 다양한 플랫폼에서 Scrapping -> Filtering Algorithm 및 tech -> 다양한 데이터 재가공 및 시각화
    - 다양한 기준에 부합한 적절한 데이터를 유저에게 제공
    - 실사용자 검증을 거친 유저로부터 데이터 수집

- 기술 스택
    - Front
    - Back
    - DBMS
    - 기타



- 약점
    - 5주 프로젝트로는 너무 쉬움



### 이sim전심 or 심sim상

- 계획서 : X, http://www.cwn.kr/news/articleView.html?idxno=9397 (비슷한 서비스 10개에 관한 기사)

- 설명 요약 : Pair programming에 도움을 주는 원격 프로그래밍 

- 선정 이유 : 정글 과정에서 하나의 노트북으로 진행한 pair programming의 불편함 개선 목적

- 핵심 기능 
    - 원격으로 단일 코딩 진행
    - 동시 입력으로 인한 부작용 방지
    - 다양한 의사소통 툴 제공

- 기술 스택
    - Front
    - Back
    - DBMS
    - 기타
- 약점
    - 내가 이게 되는건지 모르겠음



### Webbing

- 계획서 : https://github.com/junsoopooh/Studying_Algorithm/blob/main/IDEA_Collection/webbing/webbing.md

- 설명 요약 : 다양한 주제와 입력에 대해 간편하고 다양한 시각화 제공툴

- 선정 이유 : 단편화된 개념의 동기화를 제공하고 한 눈에 흐름을 파악하는데 도움을 주기 위함

- 핵심 기능
    - 특정 범위 내에서 개념간의 관계성을 알맞게 시각화
    - 다양하고 복잡한 함수 호출 Flow를 알맞게 시각화
    - 각 노드와 외부 자료(URL, 파일 등)의 연결
    - 유저가 수정하는데 보조 도구 제공
    - 다양한 시각화 형태, 유저의 다양한 입력에 대한 수용성

- 기술 스택
    - Front
    - Back
    - DBMS
    - 기타

- 약점
    - 다양한 시각화결과 필요
    - 다양한 입력에 관한 반응성 필요