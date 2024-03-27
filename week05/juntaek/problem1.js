function solution(keymap, targets) {
  let answer = [];
  let pressKey = 0;

  targets.forEach((x) => {
    for (let i = 0; i < x.length; i++) {
      let count = Infinity;
      keymap.forEach((key) => {
        let idx = key.indexOf(x[i]);

        if (idx > -1) {
          count = Math.min(count, idx + 1);
        }
      });
      pressKey += count;
    }
    answer.push(pressKey);
    pressKey = 0;
  });
  answer = answer.map((x) => {
    if (x == Infinity) {
      x = -1;
    }
    return x;
  });
  return answer;
}
