| 문제  | 회차 | 결과         | 방식                                                   | 풀이 시간 | 메모리      | 수행 시간 | 코드 길이 | 코멘트                       |
| ----- | ---- | ------------ | ------------------------------------------------------ | --------- | ----------- | --------- | --------- | ---------------------------- |
| 11725 | 1    | 오답         | 1과 연결된 노드부터 탐색                               | 30분      | X           | X         | X         | 어렵당                       |
| 11725 | 2    | 정답         | dfs                                                    | 12분 42초 | 65060KB     | 364ms     | 399B      | dfs란걸 알고나니 쉽네        |
| 1707  | 1    | 정답         | 색깔 번갈아 설정하며 DFS                               | 29분 56초 | 53244KB     | 1380ms    | 846B      | 와 풀엇                      |
| 21606 | 1    | 오답         | 실내점을 출발로 하여 실내를 만나면 카운트하며 dfs      | 30분      | X           | X         | X         | cnt가 작동이 안된다.         |
| 21606 | 2    | 38/200 정답  | 실내 지점마다 dfs                                      | 23분 36초 | 67736KB     | 528ms     | 683B      | 시간복잡도는 최악이군        |
| 20606 | 3    | 200/200 이해 | 이웃하는 실내 먼저 체크하기                            | 30분      | 113304KB    | 1328ms    | 869B      | 뺼수 있는건 미리 뺴는게 좋다 |
| 14888 | 1    | 정답         | 각 케이스별로 로직 처리 후 dfs                         | 16분 13초 | 31256KB     | 56ms      | 1205B     | 굿                           |
| 2573  | 1    | 오답         | 각 얼음의 녹는 양 체크, 재귀를 통해 존재하는 얼음 체크 | 30분      | 메모리 초과 | X         | 1489B     | 너무 복잡한 코               |
| 2573  | 2    | 정답         | 새로운 배열을 통해 얼음 배열만 탐색한다                | 27분 17초 | 33860KB     | 2904ms    | 1387B     | 이게 되네                    |
| 2617  | 1    | 오답         | 비교 가능한 구슬 번호를 포함하는 배열                  | 30분      | X           | X         | 815B      | 예외를 못찾겠다.             |
| 2617  | 2    | 정답         | 재귀를 통해 모든 깊이를 파악함                         | 28분 33초 | 31256KB     | 240ms     | 621B      | 재귀를 안썼구나!             |
