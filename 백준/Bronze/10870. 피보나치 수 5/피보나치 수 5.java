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

        int n = Integer.parseInt(br.readLine());
        int result;
        if (n == 0) {
            result = 0;
        } else if (n == 1) {
            result = 1;
        } else {
            int temp, pprev = 0;
            int prev = 1;
            for (int i = 2; i <= n; i++) {
                temp = pprev;
                pprev = prev;
                prev = temp + pprev;
            }
            result = prev;
        }
        bw.write(result + "\n");
        bw.flush();
        br.close();
        bw.close();
    }

}
