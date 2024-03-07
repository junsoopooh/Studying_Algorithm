
function solution(m, musicinfos) {
    const len = musicinfos.length;
    m = filterString(m);
    
    musicinfos = musicinfos.sort((a,b) => {
        const [a_start, a_end, a_title, a_pattern] = a.split(",");
        const [b_start, b_end, b_title, b_pattern] = b.split(",");
        
        return countTime(b_start, b_end) >= countTime(a_start, a_end) ? 1 : -1;
    })
    
    for (let i=0; i<len; i++) {
        const [start,end, title, pattern] = musicinfos[i].split(",");
        const duration = countTime(start, end);
        
        let music = filterString(pattern);
        
        while(music.length < duration) {
            music += music;
        }
        music = music.slice(0, duration+1);
        
        if (music.includes(m)) return title;
    }
        
    return "(None)";
}

// #이 붙은 문자를 하나의 문자로 치환하기
function filterString(string) {
    let result = string;
    result = result.replaceAll("A#", "1")
    result = result.replaceAll("C#", "2")
    result = result.replaceAll("D#", "3")
    result = result.replaceAll("F#", "4")
    result = result.replaceAll("G#", "5")
    return result;
}

// 재생시간 계산
function countTime(start, end) {
    const [s_H, s_M] = start.split(":");
    const [e_H, e_M] = end.split(":");
    
    const hourDiff = +e_H  - +s_H; // 숫자로 변환
    const minDiff = +e_M - +s_M;
    
    return 60 * hourDiff + minDiff;
}