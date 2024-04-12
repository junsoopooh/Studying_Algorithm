function solution(phone_book) {
  phone_book.sort(); // 왜 정렬을 시켜야 시간초과가 안 날까?

  for (let i = 0; i < phone_book.length - 1; i++) {
    if (
      phone_book[i] === phone_book[i + 1].substring(0, phone_book[i].length)
    ) {
      return false;
    }
  }

  return true;
}

function solution(phone_book) {
    phone_book.sort();
    return !phone_book.some((v, i) => phone_book[i+1]?.indexOf(v) === 0);
}

function solution(phoneBook) {
    return !phoneBook.sort().some((t,i)=> {
        if(i === phoneBook.length -1) return false;

        return phoneBook[i+1].startsWith(phoneBook[i]);
    })
}
