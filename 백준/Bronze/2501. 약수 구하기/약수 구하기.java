import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] arr = new int[n + 1];

        int idx = 1;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                arr[idx] = i;
                idx++;
            }
        }

        if (idx <= k) {
            bw.write(0 + "\n");
        } else {
            bw.write(arr[k] + "\n");
        }
        bw.flush();
        bw.close();
    }

}
