function solution(s, skip, index) {
    var alpa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
                      "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
                      "u", "v", "w", "x", "y", "z"].filter(z => !skip.includes(z));
    
    return s.split('').map((a) => alpa[(alpa.indexOf(a) + index) % alpa.length]).join('');
}

// function solution(strings, skip, index) {
//   let answer = '';
//   const alphabet = new Set('abcdefghijklmnopqrstuvwxyz');
//   [...skip].forEach(val => alphabet.delete(val));

//   const arr = [...alphabet];

//   for (const s of strings) {
//     const idx = arr.indexOf(s) + index;
//     answer += arr[idx % arr.length];
//   }

//   return answer;
// }