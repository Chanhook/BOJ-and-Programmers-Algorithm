public class Solution {

    private static String[] str = {"A", "B", "C", "D", "E", "F"};

    public String solution(int n, int t, int m, int p) {
        StringBuilder sb = new StringBuilder("0");
        StringBuilder s;
        for (int i = 1; i <= t * m; i++) {
            s = new StringBuilder();
            int tmp = i;
            while (tmp > 0) {
                int x = tmp % n;
                if (x == 10) {
                    s.append(str[0]);
                } else if (x == 11) {
                    s.append(str[1]);
                } else if (x == 12) {
                    s.append(str[2]);
                } else if (x == 13) {
                    s.append(str[3]);
                } else if (x == 14) {
                    s.append(str[4]);
                } else if (x == 15) {
                    s.append(str[5]);
                } else {
                    s.append(x);
                }
                tmp /= n;
            }
            sb.append(s.reverse());
        }

        String numStr = sb.toString();
        sb = new StringBuilder();

        int order = 1;
        for (int i = 0; i < numStr.length(); i++) {
            if (sb.length() == t) {
                break;
            }
            if (order > m) {
                order = 1;
            }
            if (order == p) {
                sb.append(numStr.charAt(i));
            }
            order++;
        }

        return sb.toString();
    }
}
