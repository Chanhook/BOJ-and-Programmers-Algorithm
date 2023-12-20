import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int maxNumber = 1000;

        boolean[] isPrime = new boolean[maxNumber + 1];
        Arrays.fill(isPrime, true);

        isPrime[1] = false;
        for (int i = 2; i * i <= maxNumber; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= maxNumber; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        int primeCount = 0;
        int N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (isPrime[num]) {
                primeCount++;
            }
        }

        bw.write(primeCount + "\n");

        bw.flush();
        br.close();
        bw.close();
    }
}
