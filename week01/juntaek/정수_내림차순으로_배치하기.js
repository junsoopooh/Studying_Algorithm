// function solution(n) {
//     // n을 하나씩 돌면서 각 자리마다 가장 큰 숫자를 업데이트 하기
//     // 그냥 문자열을 하나의 배열의 요소로 만들어서 내림차순 정렬한 후 다시 문자열로 합치면 어떰?
//     return parseInt((n + '').split('').sort((a, b) => b - a).join(''));
// }

function solution(n) {
  const newN = n + "";
  const newArr = newN.split("").sort().reverse().join("");

  return +newArr; // 문자열 앞에 +를 붙이면 숫자로 변환이 가능하다.
}
