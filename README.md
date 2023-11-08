# 씹어먹는 알고리즘

_2023년 11월 8일에 시작된 파이썬 알고리즘 스터디_

## 멤버

- [배준수](https://github.com/junsoopooh)<br>
- [서준택](https://github.com/Taek222)<br>
- [최성혁](https://github.com/Choi-Seong-Hyeok)<br><br>

## 일정

- 2023년 11월 15일 수요일 오후 8시 Zoom 회의 (추후 링크 공지 예정)

## 공지사항(2023.11.08)

- 테스트: 매월 마지막 수요일에 2문제
- 학습량 : 매주 4문제(Lv1 2문제 Lv2 2문제)로 고정됩니다.(시험 전 주는 2문제(Lv1 1문제 + Lv2 1문제))
  <br><br>

## 안내사항

- 매주 회의가 끝나면 각 주차에 해당하는 폴더가 만들어집니다.<br>

- 회의가 끝나면 지난 주차의 PR을 merge 합시다.<br>

- 지나간 주차의 파일들은 월별로 묶어서 정리됩니다.<br>

- 만들어진 폴더 안에 자신의 이름 폴더를 만들고 그 안에 해당 주차에 공부한 것들을 정리해서 올립시다.<br>

- 각 파일 제목은 무엇에 관한 파일인지 알아볼 수 있게 올립시다.<br>

- 매 주 개인 branch 생성을 생활화합시다.<br>

- 꼭 문제에 대한 답안 코드가 아니더라도, 공부했던 개념을 정리한 markdown이나 txt를 올려도 무방합니다.<br>

- README.MD 파일은 최대한 자세하게, 쓸데없는 소리까지 다 적었으면 좋겠습니다. 우리 기억은 생각보다 휘발성이 강합니다.<br>

- 지금은 의미없어 보이는 것이 나중에 기록이 되고 발자취가 됩니다.<br>

- 매일 매일 일정하게 풀면서 commit으로 기록을 남기는 건 어떨까요? 힘들지만 좋은 습관을 들여봅시다.<br>

  <br><br>

---

<br><br>

## 규칙<br>

<br>

1. 공통문제는 반드시 풀어 온다.<br>
2. 공통문제는 가능한 선에서 최대한 이해하여 남에게 설명이 가능한 수준까지 학습하여야 한다.<br>
3. 매 주차 자신의 READMD.MD에 만들어 가능한 상세하게 기록한다.<br>
4. 모르는 부분에 대해서도 명확한 질문이 가능하도록 준비하여야 한다.<br>
5. 스터디 모임은 매 주 수요일로 하되, 합의 하에 요일과 시간, 방식을 조절한다.<br>
6. 올린 Pull Request는 모임 이후 merge한다.<br>
7. 회의에 참여하지 못하는 경우 미리 통지한다.<br><br>

---

<br><br>

## Terminal(Visual Studio CODE)로 제출하는 법<br>

<br>

1. **이번주 내용 받아오기**<br>

- 새로운 폴더에 받기(사실 받을 내용은 의미없는 README.MD 뿐이지만 폴더 만들어놨으니까..)<br>
  ```sh
  $ git clone https://github.com/junsoopooh/Studying_Algorithm.git
  $ cd Studying_Algorithm.git
  ```
  <br>
- 이미 clone 해놓은 폴더에 이번주 추가하기.
  ```sh
  $ cd Studying_Algorithm.git
  $ git checkout main
  $ git pull
  ```
  <br><br>

2. **제출할 공간 만들기**<br>

```sh
$ cd ${이번주차폴더}
$ mkdir ${내영어이름}
$ cd ${내영어이름}
$ git checkout -b ${이번주차폴더}/${내영어이름}
$ git push -u origin ${이번주차폴더}/${내영어이름}
```

<br><br> 3. **push로 제출하기**
내 local에서 올릴 파이썬파일과 Markdown등을 ${이번주차폴더}/${내영어이름}<br>

```sh
$ git add .  #git add . 은 현재 디렉토리 내에 모든 변경사항을 포함시킵니다.
#example.py라는 파일만 하고싶으면 git add example.py 라고 하면 됩니다.
$ git commit -m '하고싶은 말' # 어떤문제였다던가, 나중에 질문할거라던가, 다했다던가, 어려웠다던가..., 하기싫다던가..
$ git push #
```

<br><br> 4. **[스터디 repository](https://github.com/junsoopooh/Studying_Algorithm) 이동**<br>

- branch 생성, push 확인하기<br>
- 'base:main <- compare:${이번주차폴더}/${내영어이름}' 방향 확인하기<br>
- Pull request 생성<br>
  <br><br>

5. **월요일 회의가 끝나고 자신의 PR을 merge 한다.**
   <br><br>

---

<br><br>

## git 명령어

<br><br>

```sh
$ git clone <repository URL>  # 해당 URL의 repository clone하기
$ git branch                  # 해당 repo의 브랜 목록 보기
$ git branch -r               # remote 브랜치 보기
$ git log --oneline           # 내가 위치해 있는 branch 확인
$ git branch -d <브랜치이름>   # 로컬 브랜치 삭제
$ git branch <브랜치이름>      # 브랜치 생성
$ git checkout <브랜치이름>    # 작업하는 브랜치 변경
$ git checkout -b <브랜치이름> # 위 두가지를 한번에, 즉 브랜치를 만들고 그곳을 작업 브랜치로 하기
$ git push origin <브랜치이름> # 생성한 local 브랜치를 remote 브랜치에 붙여넣기
$ git branch --set-upstream-to origin/<브랜치 이름> # local 브랜치, remote 브랜치 연동하기
```

<br><br>

```sh
$ git add .                     # 현재 디렉토리의 변경사항 모두 추적
$ git status                    # 추적상태 확인
$ git commit -m "하고싶은말"		  # 하고싶은말을 메시지로 같이 남김
$ git push 						          # 원격저장소에 업로드
```

<br><br>

```sh
$ cd <디렉토리> #해당 디렉토리(자식)로 이동
$ cd ..         #부모 디렉토리로 이동
$ ls            # 디렉토리에 존재하는 파일 목록 출력
$ ll            # ls에 -l 이라는 long option 추가로 상세히 출력
$ mkdir         # 해당 이름의 하위 디렉토리 생성
```

<br><br>
mv 명령어 옵션

```sh
$ mv [-option] [파일이름] [디렉토리]    #mv는 이동시키기
$ mv [파일이름] [변경할 파일 이름]       #존재하는 디렉토리를 넣지 않으면 해당이름으로 파일이름을 변경함.
```

옵션 종류<br>
-f : 디렉토리에 동일한 파일 이름 있어도 강제 이동<br>
-i : 디렉토리에 동일한 파일 이름 있으면 물어봄<br>
-u : 디렉토리에 있는 파일이 더 최신이면 이동하지 않음<br>
<br><br>

---

rm 명령어 옵션

```sh
$ rm [-option] [파일이름] #rm은 삭제시키기
```

옵션 종류<br>

-i : 삭제할지 여부 물어봄<br>
-r : 하위 디렉토리까지 모두 삭제<br>
<br><br>

---

git master(main)으로 내 local 덮어쓰기

```sh
$ git fetch -all
$ git reset --hard origin/master
```

master가 아닌 다른 branch로 덮어쓰기

```sh
$ git fetch -all
$ git reset --hard origin/<브랜치 이름>
```

현재 local을 다른 branch에 저장한 후, git pull로 덮어쓰기

```sh
$ git checkout master
$ git branch <브랜치 이름>
$ git fetch --all
$ git reset --hard origin/master
```

<br><br>

---

git config 설정 관련(git config 관련 오류가 나올 시 유용)

```sh
$ git config --list #전체 config 리스트 확인

#git config 설정하기(둘 다 해주어야 함)
$ git config --global user.name "홍길동"
$ git config --global user.email "id@email.com"

# git config 삭제하기
$ git config --unset user.name
$ git config --unset user.email

#삭제해도 남아있는 경우는 global 옵션 때문일 가능성이 있음. 이 경우 아래 방법으로 지울 수 있음
$ git config --unset --global user.name
$ git config --unset --global user.email
```
