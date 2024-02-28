function solution(board, moves) {
  // 인형이 없는 칸은 빈칸
  // 격자의 아래 칸부터 차고차곡
  // 크레인을 좌우로 움직여 멈춘 위치에서 가장 위에 있는 인형 집어듬
  // 집어 올린 인형은 바구니에 쌓임.
  // 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 큼!
  // 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 리턴!
  // board[i][j]가 있을 때 moves에 따라서 j를 고정시키고, i를 돌면서 해당 값이 나오는 순간
  // 그 값을 stack에 넣고 board[i][j] 값을 0으로 고침.
  // 그리고나서 stack[stack.length - 1] === board[i][j]가 같다? 그럼 stack.pop()하고
  // result += 1
  const stack = [];
  let result = 0;
  for (let i = 0; i < moves.length; i++) {
    for (let j = 0; j < board.length; j++) {
      if (board[j][moves[i] - 1] !== 0) {
        if (stack[stack.length - 1] === board[j][moves[i] - 1]) {
          stack.pop();
          result += 1;
        } else {
          stack.push(board[j][moves[i] - 1]);
        }
        board[j][moves[i] - 1] = 0;
        console.log("stack", stack);
        break;
      }
    }
  }
  console.log("result", result);
  return result;
}
