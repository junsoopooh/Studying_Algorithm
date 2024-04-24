function solution(prices) {
  var answer = [];
  for (let i = 0; i < prices.length; i++) {
    let count = 0; // 각 주식 가격에 대해 시간 카운트를 초기화
    for (let j = i + 1; j < prices.length; j++) {
      if (prices[i] <= prices[j]) {
        count += 1;
      } else {
        count += 1; // 가격이 떨어진 직후에도 시간을 하나 추가해야 하므로
        break;
      }
    }
    answer.push(count); // 내부 루프가 종료된 후 count를 answer 배열에 추가
  }
  return answer;
}
