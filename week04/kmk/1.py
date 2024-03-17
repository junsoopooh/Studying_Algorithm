"""
음양 더하기
문제: https://school.programmers.co.kr/learn/courses/30/lessons/76501
"""
def solution(a, s):
    answer = 0
    for i in range(len(a)):
        a[i] = a[i] if s[i] else -a[i]
        answer += a[i]
    return answer

"""
class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        
        for (int i = 0; i < absolutes.length; i++) {
            absolutes[i] = signs[i] ? absolutes[i] : -absolutes[i];
            answer += absolutes[i];
        }
        
        return answer;
    }
}
"""