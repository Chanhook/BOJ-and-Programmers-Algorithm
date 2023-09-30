import java.util.*;
class Solution {
    boolean solution(String s) {
        ArrayDeque<Character> tempList = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (tempList.isEmpty() && c == ')') {
                return false;
            }

            if (c == '(') {
                tempList.add(c);
                continue;
            }

            if (c == ')') {
                tempList.pop();
            }
        }

        if (!tempList.isEmpty()) {
            return false;
        }
        return true;
    }
}