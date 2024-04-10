function solution(babbling) {
  var answer = 0;
  var arr = ["aya", "ye", "woo", "ma"];

  for (var i = 0; i < babbling.length; i++) {
    let bab = babbling[i];

    for (var j = 0; j < arr.length; j++) {
      if (bab.includes(arr[j].repeat(2))) {
        break;
      }
      bab = bab.split(arr[j]).join(" ");
    }
    if (bab.split(" ").join("").length === 0) {
      answer++;
    }
  }
  return answer;
}
