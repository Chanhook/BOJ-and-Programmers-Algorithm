import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int maxNum = 10000;
        boolean[] isPrime = new boolean[maxNum + 1];
        Arrays.fill(isPrime, true);

        isPrime[1] = false;
        for (int i = 2; i * i <= maxNum; i++) {
            if (isPrime[i]) {
                for (int j = i + i; j <= maxNum; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        int m = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        int minPrime = 0;
        int total = 0;
        for (int i = m; i <= n; i++) {
            if (isPrime[i]) {
                if (minPrime == 0) {
                    minPrime = i;
                }
                total += i;
            }
        }
        if (total == 0) {
            bw.write(-1 + "\n");
        } else {
            bw.write(total + "\n");
            bw.write(minPrime + "\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
