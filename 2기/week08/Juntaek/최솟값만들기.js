// 나의 풀이 (not solved)
function solution(A, B) {
  var answer = 0;

  // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
  console.log("Hello Javascript");

  // 배열 a,b가 주어질 때 최종적으로 누적된 최솟값을 리턴하는 함수 완성!
  // a에서는 최솟값 b에서는 최댓값 뽑는 식으로 곱해서 더하는 느낌!
  for (let i = 0; i < A.length; i++) {
    const maxValue = Math.max.apply(null, A);
    const minValue = Math.min.apply(null, B);
    console.log("maxValue", maxValue);
    console.log("minValue", minValue);
    A.filter((value) => value != maxValue);
    B.filter((value) => value != minValue);
    console.log("a, b", A, B);
    answer += maxValue * minValue;
    console.log("answeranswer", answer);
  }

  return answer;
}

//다른 사람의 풀이
function solution(A, B) {
  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);
  return A.reduce((total, val, idx) => total + val * B[idx], 0);
}
