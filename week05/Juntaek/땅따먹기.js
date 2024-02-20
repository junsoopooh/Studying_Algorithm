function solution(land) {
    var answer = 0;

    // 땅따먹기 게임
    // n행 4열, 모든 칸에는 점수
    // 각 행의 4칸 중 한 칸만 밟으면서 내려와야 한다.
    // 단, 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없다.
    // 마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최댓값을 리턴하는 함수를 완성해 주세요!
    // 각 행마다 4칸을 다 돌면서 가장 큰 값을 변수에 담고 그때의 인덱스 값 기억
    // 그 다음행에서 가장 큰 값을 변수에 담기 단, 이전 행에서 기억한 인덱스 값과 같으면 안됨.
    let n = land.length
    let max_num = 0;
    let max_index = 5;
    let ret_idx = 0;
    console.log(n)
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < 4; j++) {
            if ((max_num < land[i][j]) && (ret_idx != j)) {
                max_num = land[i][j]
                max_index = j
                // console.log(max_num, max_index)
            }
        }
        answer += max_num
        ret_idx = max_index
        max_num = 0
    }

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    // console.log('Hello Javascript')

    return answer;
}



// 다른 사람 풀이 1
function solution(land) {
  let answer = [];
  let len = land.length;
  for (let i = 1; i < len; i++) {
    land[i][0] += Math.max(land[i - 1][1], land[i - 1][2], land[i - 1][3]);
    land[i][1] += Math.max(land[i - 1][0], land[i - 1][2], land[i - 1][3]);
    land[i][2] += Math.max(land[i - 1][0], land[i - 1][1], land[i - 1][3]);
    land[i][3] += Math.max(land[i - 1][0], land[i - 1][1], land[i - 1][2]);
  }
  answer = land[land.length - 1];

  return Math.max(...answer);
}

// 다른 사람 풀이 2
function solution(land) {
  var answer = 0;

  return Math.max(
    ...land.reduce(
      (a, c) => {
        return [
          c[0] + Math.max(a[1], a[2], a[3]),
          c[1] + Math.max(a[0], a[2], a[3]),
          c[2] + Math.max(a[0], a[1], a[3]),
          c[3] + Math.max(a[0], a[1], a[2]),
        ];
      },
      [0, 0, 0, 0]
    )
  );
}
