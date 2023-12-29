import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    static int n, k;
    static int maxValue = Integer.MIN_VALUE;
    static boolean[] learn;
    static String[] words;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        words = new String[n];
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            s = s.replace("anta", "");
            s = s.replace("tica", "");
            words[i] = s;
        }

        if (k < 5) {
            bw.write(0 + "\n");
        } else if (k == 26) {
            bw.write(n + "\n");
        } else {
            learn = new boolean[26];
            learn['a' - 'a'] = true;
            learn['c' - 'a'] = true;
            learn['i' - 'a'] = true;
            learn['n' - 'a'] = true;
            learn['t' - 'a'] = true;

            backtracking(0, 0);
            bw.write(maxValue + "\n");
        }

        bw.flush();
    }

    private static void backtracking(int alp, int len) {
        if (len == k - 5) {
            int count = 0;
            for (int i = 0; i < n; i++) {
                boolean readable = true;
                for (int j = 0; j < words[i].length(); j++) {
                    if (!learn[words[i].charAt(j) - 'a']) {
                        readable = false;
                        break;
                    }
                }
                if (readable) {
                    count++;
                }
            }
            maxValue = Math.max(count, maxValue);
            return;
        }

        for (int i = alp; i < 26; i++) {
            if (!learn[i]) {
                learn[i] = true;
                backtracking(i, len + 1);
                learn[i] = false;
            }
        }

    }
}
