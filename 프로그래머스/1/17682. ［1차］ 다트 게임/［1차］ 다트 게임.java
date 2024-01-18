import java.util.*;
class Solution {
    public int solution(String dartResult) {
        int[] arr = {1, 1, 1};
        int idx = 0;

        LinkedList<Character> q = new LinkedList<>();
        for (char ch : dartResult.toCharArray()) {
            q.add(ch);
        }

        String tmp = "";
        while (!q.isEmpty()) {
            char x = q.poll();

            // S, D, T
            if (Character.isAlphabetic(x)) {
                int base = Integer.parseInt(tmp.toString());
                int exponent = 0;
                if (x == 'S') {
                    exponent = 1;
                } else if (x == 'D') {
                    exponent = 2;
                } else {
                    exponent = 3;
                }
                arr[idx++] *= Math.pow(base, exponent);
                tmp = "";
            } else {
                if (x == '*') {
                    arr[idx - 1] *= 2;
                    if (idx > 1) {
                        arr[idx - 2] *= 2;
                    }
                } else if (x == '#') {
                    arr[idx - 1] *= -1;
                } else {
                    tmp += x;
                    continue;
                }
            }
        }

        int answer = Arrays.stream(arr).sum();
        return answer;
    }
}