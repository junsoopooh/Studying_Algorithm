
1. 퀵정렬 
a. 매 재귀호출 단계마다 피벗의 left, right 리스트 만들었는데 이러면 공간 O(n)
b. 주석처리하고 재귀호출마다 피벗의 left, right 만들지 않는 in-place 퀵정렬로 변경(다른사람 코드봄) - 공간 O(1)
2. 그림부터가 스택이라 스택으로 품
3. 2번문제랑 비슷한 아이디어인듯
4. 하라는대로 하면 돼서 오히려 간단한 문제인데 문제는 하라는대로 하기가 힘듬
- 네개 겹쳐서 삭제하려는 요소가 중복되는 문제
- 어떻게 떨굴것인지(나는 각 칼럼의 아래요소부터 밑으로 떨굴 수 있는지 확인해보고 떨굼)
- 이러한 과정에서 인덱스 안벗어나고, row/col 값 관리하는게 어려웠음
- 뇌버깅으로는 못풀겠어서 디버거 돌려가면서 품

