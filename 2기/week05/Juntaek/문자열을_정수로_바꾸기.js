// 나의 풀이.. 뻘짓 오지게 함..
function solution(s) {
  var answer = 0;
  let ret = new Array();
  for (let i = 0; i < s.length; i++) {
    if (s[i] == "+") {
      continue;
    } else if (s[i] == "-") {
      answer = -1;
    } else {
      ret.push(parseInt(s[i]));
      console.log(ret);
    }
  }
  ret.join(", ");
  console.log("ret", ret);
  return answer * ret;
}

// 다른 사람풀이 1
function solution(s) {
  return Number(s);
}

// 2
function solution(s) {
  return parseInt(s);
}
// 3
function strToInt(str) {
  return str/1
}
