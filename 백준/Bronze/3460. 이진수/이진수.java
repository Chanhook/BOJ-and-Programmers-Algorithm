import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(out));

        int T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {
            int n = Integer.parseInt(br.readLine());
            StringBuilder sb = new StringBuilder();
            while (n > 0) {
                int i = n % 2;
                if (i == 1) {
                    sb.append(i);
                } else {
                    sb.append(i);
                }
                n /= 2;
            }

            for (int i = 0; i < sb.length(); i++) {
                if (sb.charAt(i) == '1') {
                    bw.write(i + " ");
                }
            }
            bw.write("\n");
        }

        bw.flush();
        br.close();
        bw.close();
    }

}
