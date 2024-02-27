function solution(s) {
  // 알파벳이 같은 알파벳 2개 붙어 있는 짝 찾기..
  // 그 둘을 제거한 뒤, 앞뒤로 문자열 이어 붙이기
  // 이 과정 모두 반복하여 문자열 모두 제거한다면 제거하기 종료!
  // 짝지어 제거하기 성공적으로 수행할 수 있는지 반환하는 함수를 완성하자!
  // 성공 시 1 리턴, 아닐 경우 0 리턴!
  // 자스 배열에서 push, pop을 이용할수가 있다?
  // 아래와 같이 코드를 짜면 중간에 짝지어 제거된 후 바로 이전 데이터와 그 다음데이터가 같을 때 짝지어 제거가 불가능.
  // const newArr = s.split('');
  // for (let i = 0; i < newArr.length-1; i++) {
  //     console.log("newArr[i]", newArr[i])
  //     console.log('newArr', newArr)
  //     if (newArr[i] === newArr[i+1]) {
  //         // 해당 값을 s의 배열에서 제거하기??
  //         newArr.splice(i, 2);
  //         console.log('newArr', newArr)
  //     }
  // }
  // return newArr.length === 0 ? 1 : 0

  const stack = [];

  for (let i = 0; i < s.length; i++) {
    if (stack[stack.length - 1] === s[i]) {
      stack.pop();
    } else {
      stack.push(s[i]);
    }
  }
  return stack.length ? 0 : 1;
}
