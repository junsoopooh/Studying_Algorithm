// 나의 풀이 (93.3/100)
function solution(s) {
  var answer = true;

  var lower_str = s.toLowerCase();

  // 대문자 소문자 섞여 있는 문자열에서 p와 y의 개수를 비교해 같으면 true
  // p, y 모두 하나도 없는 경우 항상 true리턴!
  // 개수 비교시 대소문자 구별 x

  // s를 대문자 혹은 소문자로 바꿔준다.
  // 길이가 50이하니까 for문 돌면서 개수 세기?
  // 자스에 count함수가 있을까?
  // 있다면 p의 개수세고 y개수 세서 비교 하면 될 듯

  // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
  console.log(lower_str);
  var p_count = lower_str.split("p").length - 1;
  var y_count = lower_str.split("y").length - 1;
  if (p_count == 0 || y_count == 0) {
    return false;
  } else if (p_count === y_count) {
    return true;
  } else {
    return false;
  }
}

// 나의 풀이 (100점)
function solution(s) {
  var answer = true;

  var lower_str = s.toLowerCase();
  console.log(lower_str);
  var p_count = lower_str.split("p").length - 1;
  var y_count = lower_str.split("y").length - 1;

  if (p_count === y_count) {
    return true;
  } else {
    return false;
  }
}

// 다른 사람의 풀이 1
function solution(s) {
  return (
    s.toUpperCase().split("P").length === s.toUpperCase().split("Y").length
  );
}

// 다른 사람의 풀이 2
function solution(s) {
  return s.match(/p/ig).length == s.match(/y/ig).length;
}