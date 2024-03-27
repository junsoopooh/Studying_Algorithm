function solution(msg) {
  var answer = [];
  // 1.index가 색인번호 되도록 사전 초기화
  var dic = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
  ];

  while (msg.length !== 0) {
    var w = "";
    var wc = "";

    for (var i = 0; i < msg.length; i++) {
      w = msg.slice(0, i);
      wc = msg.slice(0, i + 1);
      if (dic.indexOf(wc) === -1) {
        // wc가 사전에 없으면
        answer.push(dic.indexOf(w) + 1); // w의 색인번호를 출력 (index+1)
        break;
      }
      if (i === msg.length - 1) {
        // ***마지막 문자의 경우
        answer.push(dic.indexOf(wc) + 1); // wc의 색인번호를 출력
      }
      // console.log('answer', answer)
    }

    dic.push(wc); // 사전에 없는 경우 dic에 wc 넣기
    msg = msg.slice(i); //msg에서 w 제거
  }
  return answer;
}
