"""
다리를 지나는 트럭
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42583
"""

from collections import deque
def solution(b, w, t):
    """
    1. 변수명 길어서 그냥 줄여줌
    2. 트럭 앞에서부터 빼기 위해 덱 변환
    3. 현재 무게, 현재 다리를 만들어줌. 이 때, 다리는 시간초길이로 만들어줌
    4. 루프돌면서 1초마다 트럭이 맨 뒤에 있으면 없애주고 아니면 앞에 0 넣어서 밀어줌
    5. 트럭이 --> 이 방향으로 밀린다고 보면됨
    6. 트럭다빼면 루프 종료하는데 이 때 다리위에는 트럭들 무조건있으므로 마지막에 시간 더해 줌
    """
    ans, t = 0, deque(t)

    cur_w, cur_b = 0, deque([0] * b)

    while t:
        cur_w -= cur_b.pop()
        ans += 1

        if t[0] + cur_w <= w:  # 트럭올라갈 수 있으므로 올려주고 무게도 올려줌
            cur_b.appendleft(t.popleft())
            cur_w += cur_b[0]
        else:  # 못 올라가면 그냥 맨 앞에 0 넣어주면 됨
            cur_b.appendleft(0)
    return ans + b

"""
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Deque<Integer> dq = new ArrayDeque<>();

        for (int t : truck_weights) {
            dq.add(Integer.valueOf(t));
        }

        int cur_weight = 0;
        Deque<Integer> cur_t = new ArrayDeque<>();

        for (int i=0; i<bridge_length; i++) {
            cur_t.add(Integer.valueOf(0));
        }

        while (dq.size() != 0) {
            cur_weight -= cur_t.removeLast();
            answer += 1;

            if (dq.getFirst() + cur_weight <= weight) {
                cur_t.addFirst(dq.removeFirst());
                cur_weight += cur_t.getFirst();
            } else {
                cur_t.addFirst(Integer.valueOf(0));
            }
        }

        return answer + bridge_length;
    }
}
"""