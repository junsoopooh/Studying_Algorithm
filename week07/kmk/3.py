"""
전화번호 목록
https://school.programmers.co.kr/learn/courses/30/lessons/42577
"""
"""
숫자 사전순으로 정렬 후 포함 여부 파악하면 됨
또는
트라이 알고리즘 사용
"""

def solution(p):
    p.sort()

    for i in range(len(p) - 1):
        if p[i + 1].startswith(p[i]):
            return False

    return True


"""
import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        List<String> keys = new ArrayList<>();
        
        Trie trie = new Trie();
        
        for (String p : phone_book) {
            trie.insert(p);
            keys.add(p);
        }
        
        for (String key: keys) {
            if (trie.search(key)) {
                answer = false;
                break;
            }
        }
        
        return answer;
    }
    static class TrieNode {
        Map<Character, TrieNode> childNode = new HashMap<>();
        boolean terminal;
    }

    static class Trie {
        TrieNode rootNode = new TrieNode();

        void insert(String str) {
            TrieNode node = this.rootNode;

            for (int i=0; i<str.length(); i++) {
                node = node.childNode.computeIfAbsent(str.charAt(i), key -> new TrieNode());
            }
            node.terminal = true;
        }
        boolean search(String str) {
            TrieNode node = this.rootNode;

            for (int i=0; i<str.length(); i++) {
                node = node.childNode.getOrDefault(str.charAt(i), null);

                if (node == null) {
                    return false;
                }
            }

            if (node.terminal) {
                if (node.childNode.isEmpty()) {
                    return false;
                }
            }

            return node.terminal;
        }
    }
}
"""