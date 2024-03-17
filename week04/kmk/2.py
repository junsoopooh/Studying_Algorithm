"""
체육복
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42862
"""
"""
1. 체육수업 참가할 수 있는지 체크하는 배열 선언
2. lost, reserve에 공통으로 있는 학생과 어디에도 없는 학생은 무조건 참가표시
3. reserve 딕셔너리로 변환해서 lost 배열 순회하면서 무조건 자기보다 1작은 학생 체육복 빌리는게 함(lost 정렬해야 함)
4. 마지막으로 안빌려준 학생도 참가 표시하고 리턴하면 됨
"""
from collections import Counter
def solution(n, lost, reserve):
    check = [0] * (n + 1)

    for i in range(1, n + 1):
        if i not in lost + reserve:  # 어디에도 없음
            check[i] = 1
        elif i in lost and i in reserve:  # 둘 다 있음
            check[i] = 1

    dic = Counter(reserve)
    lost.sort()

    for num in lost:
        if check[num]:
            continue
        if num - 1 in reserve and dic[num - 1] == 1 and not check[num - 1]:
            dic[num - 1] = 0
            check[num], check[num - 1] = 1, 1
        elif num + 1 in reserve and dic[num + 1] == 1 and not check[num + 1]:
            dic[num + 1] = 0
            check[num], check[num + 1] = 1, 1

    for num in reserve:
        if not check[num]:
            check[num] = 1

    return sum(check)

"""
public class PG_42862 {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;

        boolean [] answerCheck = new boolean[n+1];

        boolean [] lostCheck = new boolean[n+1];
        boolean [] reserveCheck = new boolean[n+1];

        for (int i = 0; i < lost.length; i++) {
            lostCheck[lost[i]] = true;
        }

        for (int i = 0; i < reserve.length; i++) {
            reserveCheck[reserve[i]] = true;
        }

        for (int i = 1; i < n+1; i++) {
            if (lostCheck[i] && reserveCheck[i]) {
                answerCheck[i] = true;
            } else if (!lostCheck[i] && !reserveCheck[i]) {
                answerCheck[i] = true;
            }
        }

        Arrays.sort(lost);
        
        Map<Integer, Integer> map = new HashMap<>();

        for (int num : reserve) {
            map.put(num, 1);
        }

        for (int num : lost) {
            if (answerCheck[num]) {
                continue;
            }

            if (map.containsKey(num-1) && map.get(num-1) == 1 && !answerCheck[num-1]) {
                map.put(num-1, 0);
                answerCheck[num] = true;
                answerCheck[num-1] = true;
            } else if (map.containsKey(num+1) && map.get(num+1) == 1 && !answerCheck[num+1]) {
                map.put(num+1, 0);
                answerCheck[num] = true;
                answerCheck[num+1] = true;
            }
        }

        for (int i : reserve) {
            if (!answerCheck[i]) {
                answerCheck[i] = true;
            }
        }

        for (boolean b : answerCheck) {
            if (b) {
                answer += 1;
            }
        }

        return answer;
    }
}
"""