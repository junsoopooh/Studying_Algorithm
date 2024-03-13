// function solution(a, b) {
//     var answer = 0;
//     if (a < b) {
//         for (let i = a; i <= b; i++) {
//         answer += i;
//         }
//     } else if (a >= b) {
//         for (let i = b; i <= a; i++) {
//         answer += i;
//         }
//     }

//     return answer;
// }

function solution(a, b) {
  let answer = 0;
  for (let i = Math.min(a, b); i <= Math.max(a, b); i++) {
    answer += i;
  }

  return answer;
}
