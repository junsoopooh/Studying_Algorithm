# Studying_Algorithm
*2023년 4월 3일에 시작된 정글 6기 파이썬 알고리즘 스터디*

## 공지사항
- 2023.04.13 기준으로 없습니다. 종종 업데이트할 예정입니다.<br><br>
***
<br><br>
## 안내사항
- 매주 월요일 회의가 끝나면 각 주차에 해당하는 폴더를 만들 예정입니다.<br>
- 회의가 끝나면 지난 주차의 PR을 merge 합시다.<br>
- 만들어진 폴더 안에 자신의 이름 폴더를 만들고 그 안에 해당 주차에 공부한 것들을 정리해서 올립시다.<br>
- 각 파일 제목은 무엇에 관한 파일인지 알아볼 수 있게 올립시다.<br>
- ~~우리끼리인데 브랜치 만들고 복잡하게 할 필요 있겠습니까~~<br>
- branch 생성을 생활화합시다.<br>
- 꼭 문제에 대한 답안 코드가 아니더라도, 공부했던 개념을 정리한 markdown이나 txt를 올려도 무방합니다.<br>
- private이기 때문에 우리 네명만 볼 수 있습니다.<br>
- README.MD 파일은 최대한 자세하게, 쓸데없는 소리까지 다 적었으면 좋겠습니다. 우리 기억은 생각보다 휘발성이 강합니다.<br>
- 지금은 의미없어 보이는 것이 나중에 기록이 되고 발자취가 됩니다.<br><br>

***
<br><br>
## 규칙(23.04.10 월요일 제정)<br>
<br>
1. 공통문제는 반드시 풀어 온다.<br>
1. 공통문제는 가능한 선에서 최대한 이해하여 남에게 설명이 가능한 수준까지 학습하여야 한다.<br>
1. 이외의 추가적인 문제풀이는 개인의 자유이다.<br>
1. 회의는 매주 월요일 오전 10시이다.<br>
1. 올린 Pull Request는 월요일 모임 이후 merge한다.<br>
1. 매 주차 READMD.MD 를 만들어 가능한 상세하게 기록한다.<br><br>


***
<br><br>
## Terminal(VS CODE)로 제출하는 법<br>
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
  <br><br>
3. **push로 제출하기**
  내 local에서 올릴 파이썬파일과 Markdown등을 ${이번주차폴더}/${내영어이름}<br>
  ```sh
  $ git add .  #git add . 은 현재 디렉토리 내에 모든 변경사항을 포함시킵니다. 
  #example.py라는 파일만 하고싶으면 git add example.py 라고 하면 됩니다. 
  $ git commit -m '하고싶은 말' # 어떤문제였다던가, 나중에 질문할거라던가, 다했다던가, 어려웠다던가..., 하기싫다던가..
  $ git push # 
  ```
<br><br>
4. **[스터디 repository](https://github.com/junsoopooh/Studying_Algorithm) 이동**<br>
  - branch 생성, push 확인하기<br>
  - 'base:main <- compare:${이번주차폴더}/${내영어이름}' 방향 확인하기<br>
  - Pull request 생성<br>
 <br><br>
5. **월요일 회의가 끝나고 자신의 PR을 merge 한다.**
<br><br>
***
<br><br>
## git 명령어
<br><br>

```sh
$ git clone <repository URL>  # 해당 URL의 repository clone하기
$ git branch                  # 해당 repo의 branch 목록 보기
$ git log --oneline           # 내가 위치해 있는 branch 확인 
$ git branch <브랜치이름>      # 브랜치 생성
$ git checkout <브랜치이름>    # 작업하는 브랜치 변경
$ git checkout -b <브랜치이름> # 위 두가지를 한번에, 즉 브랜치를 만들고 그곳을 작업 브랜치로 하기
```
<br><br>

```sh
$ git add . 
$ git status
$ git commit -m "하고싶은말"
$ git push 
```
<br><br>

```sh
$ cd <디렉토리>
$ cd ..
$ ls
$ ll
$ mkdir
```
<br><br>
mv 명령어 옵션
```sh
$ mv [-option] [파일이름] [디렉토리]
$ mv [파일이름] [변경할 파일 이름] #존재하는 디렉토리를 넣지 않으면 해당이름으로 파일이름을 변경함.
```

옵션 종류<
-f : 디렉토리에 동일한 파일 이름 있어도 강제 이동<br>
-i : 디렉토리에 동일한 파일 이름 있으면 물어봄<br>
-u : 디렉토리에 있는 파일이 더 최신이면 이동하지 않음<br>
<br><br>

rm 명령어 옵션
```sh
$ rm [-option] [파일이름]
```
-i : 삭제할지 여부 물어봄<br>
-r : 하위 디렉토리까지 모두 삭제














