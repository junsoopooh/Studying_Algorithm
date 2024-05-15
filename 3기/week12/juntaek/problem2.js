function solution(n, m, section) {
  let answer = 0;

  let part = 0;

  section.forEach((n) => {
    if (n > part) {
      part = n + m - 1;
      answer++;
    }
  });
  return answer;
}
