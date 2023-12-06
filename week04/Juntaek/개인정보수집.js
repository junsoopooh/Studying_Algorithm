// function solution(today, terms, privacies) {
//     var answer = [];
//     // 개인정보 n개가 존재
//     // 개인 정보는 유효기간 전까지만 보관 가능. 지나면 반드시 파기!
//     // 오늘 날짜로 파기해야 할 개인정보 번호들을 구하려 한다.
//     // 모든 달은 28일까지 있다.
//     // 유효기간은 달이다. 1 <= 유효기간 <= 100

//     // 만약에 유효기간 달(terms) + privacies 달을 더한게 12이하이면? 그냥 더한 값이랑 today랑 계산하면 됨
//     // 근데 만약에 12이상이다? 이때부터 문제
//     // 결과 %= 12 인 값을 년도에 더해줘야 함.

//     // 결과값 비교할때는 privacies의 년도부터 비교.
//     // 년도가 같다? 결과값의 달이 today의 달보다 크면 짤, 작으면 성공
//     // 년도가 다르다? today의 년도보다 크면 짤
//     return answer;
// }

function solution(today, terms, privacies) {
  const answer = [];

  // 들어온 today를 Date형식으로 바꿔줍니다.
  // YYYY.MM.DD 포멧도 지원해서 그냥 넣기만 하면 변환됩니다.
  const expire = new Date(today);

  // terms를 쉽게 찾기위해 객체화해줍니다.
  const termType = {};
  terms.forEach((item) => {
    // split() 메서드로 분리한 타입과 기간을
    // 구조 분해 할당으로 변수화 한다.
    const [type, term] = item.split(" ");

    // 타입에 기간이 얼만지 객체로 생성한다.
    // ex) 'A': 6
    termType[type] = Number(term);
  });

  // 개인정보 수집일자를 확인한다.
  privacies.forEach((item, idx) => {
    // 위와 마찬가지로 구조 분해 할당을 한다.
    const [date, type] = item.split(" ");

    // 구한 date는 new Date() 메서드를 통해 Date 형식으로 변환한다.
    const chDate = new Date(date);

    // 그리고 Date의 매서드인 setMonth를 이용해
    // chDate의 현재 달 + 타입의 기간을 더한 값을 구한다.
    chDate.setMonth(chDate.getMonth() + termType[type]);

    // 마지막으로 오늘 날짜와 구한 유효기간을 비교해
    // 유효기간이 오늘 보다 작거나 같으면 answer에 번호를 푸쉬해준다.
    if (chDate <= expire) answer.push(idx + 1);
  });

  return answer;
}
