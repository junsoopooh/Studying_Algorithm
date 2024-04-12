function isPrime(n) {
  if (n < 2) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
}

function dfs(set, arr, fixed) {
  if (arr.length >= 1) {
    for (let i = 0; i < arr.length; i++) {
      let newFixed = fixed + arr[i];
      let copyArr = [...arr];
      copyArr.splice(i, 1);

      if (isPrime(parseInt(newFixed))) {
        set.add(parseInt(newFixed));
      }
      dfs(set, copyArr, newFixed);
    }
  }
}

function solution(numbers) {
  let nums = numbers.split("");
  let set = new Set();

  dfs(set, nums, "");

  console.log(set);

  return set.size;
}
