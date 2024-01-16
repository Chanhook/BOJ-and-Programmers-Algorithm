import java.util.*;
class Solution {
    
    public class TrieNode {

        HashMap<Character, TrieNode> children = new HashMap<>();
        TrieNode parent = null;
        boolean isEnd = false;
    }

    public class Trie {

        TrieNode root = new TrieNode();

        void insert(String word) {
            TrieNode node = this.root;
            for (int i = 0; i < word.length(); i++) {
                TrieNode parent = node;
                node = node.children.computeIfAbsent(word.charAt(i), k -> new TrieNode());
                node.parent = parent;
            }
            node.isEnd = true;
        }

        int calculateInputCount(String word) {
            TrieNode node = this.root;

            for (int i = 0; i < word.length(); i++) {
                node = node.children.get(word.charAt(i));
            }

            //leaf 아닌 경우
            if (!node.children.isEmpty()) {
                return word.length();
            }

            //leaf 인 경우
            int count = 0;
            while (true) {
                node = node.parent;
                if (node.children.size() > 1 || node.isEnd) {
                    break;
                }
                count++;
            }

            return word.length() - count;
        }
    }

    public int solution(String[] words) {
        Trie trie = new Trie();

        for (String word : words) {
            trie.insert(word);
        }

        int answer = 0;
        for (String word : words) {
            answer += trie.calculateInputCount(word);
        }

        return answer;
    }
}