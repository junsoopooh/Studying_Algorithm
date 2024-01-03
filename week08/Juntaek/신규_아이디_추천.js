//다른 사람의 풀이

function solution(new_id) {
  let lower = new_id.toLowerCase();

  let level2 = lower.match(/[a-z0-9-_.]/g).join("");

  let level3 = level2.replace(/\.+/g, ".");

  let level4 = level3.replace(/^\.|\.$/g, "");

  let level5 = level4.length === 0 ? "a" : level4;

  let level6 = level5;

  if (level5.length >= 16) {
    level6 = level5.slice(0, 15).replace(/\.$/g, "");
  }

  if (level5.length <= 2) {
    let small = [...level5].pop().repeat(3 - level5.length);
    level6 += small;
    console.log(small);
  }

  return level6;
}
