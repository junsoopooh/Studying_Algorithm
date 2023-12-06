function solution(n) {
  var answer = 0;
  const dp = Array.from({ length: n / 2 + 1 }, () => 0);
  dp[1] = 3;
  dp[2] = 11;

  for (let num = 3; num <= n / 2; num++) {
    let tmpVal = dp[num - 1] * 3 + (dp[num - 1] - dp[num - 2]);
    dp[num] = tmpVal > 0 ? tmpVal % 1000000007 : tmpVal + 1000000007;
  }
  return dp[n / 2];
}
