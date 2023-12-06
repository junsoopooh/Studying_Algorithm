function solution(num) {
  var answer = "";
  // num % 2 = 0 이면 짝수 Even 반환
  // num % 2 = 1 이면 홀수 Odd 반환
  if ((num %= 2) == 0) {
    answer = "Even";
    return answer;
  } else {
    answer = "Odd";
    return answer;
  }
}

function evenOrOdd(num) {
  return num % 2 ? "Odd" : "Even";
}
