// 내 풀이
function solution(n) {
  var answer = 0;
  let dp = new Array(n + 1);
  dp[0] = 0;
  dp[1] = 1;
  dp[2] = 2;
  for (let i = 3; i < dp.length; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
  }
  answer = dp[n];
  return answer;
}

// n = 1 : 1번
// n = 2 : 11, 2 2번
// n = 3 : 11, 12, 21 3번
// n = 4 : 1111, 121, 211, 112, 22, 5번
// n = 5 : 11111, 1112, 1121, 1211, 2111, 122, 212, 221 8번
// fn = fn-1 + fn-2
// n = 0 : 0

// 다른 사람의 풀이1
function solution(n) {
  const dp = Array.from({length:n}).fill(0);
  dp[0] = 1, dp[1] = 1;

  for (let i = 2; i <= n; i++) {
    dp[i] = (dp[i-2] + dp[i-1]) % 1234567;
  }

  return dp[n];
}

// 다른 사람의 풀이2
function jumpCase(num) {
  if (num === 1) return 1
  if (num === 2) return 2

  return jumpCase(num-1) + jumpCase(num-2)
}

