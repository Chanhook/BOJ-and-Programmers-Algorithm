import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int num1 = Integer.parseInt(st.nextToken());
        int num2 = Integer.parseInt(st.nextToken());

        if (num1 < num2) {
            int temp = num1;
            num1 = num2;
            num2 = temp;
        }

        bw.write(gcd(num1, num2) + "\n");
        bw.write(lcm(num1, num2) + "\n");

        bw.flush();
        br.close();
        bw.close();
    }

    private static int lcm(int num1, int num2) {
        return num1 * num2 / gcd(num1, num2);
    }

    private static int gcd(int num1, int num2) {
        if (num2 == 0) {
            return num1;
        }
        return gcd(num2, num1 % num2);
    }

}
