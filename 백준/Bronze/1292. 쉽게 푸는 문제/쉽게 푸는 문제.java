import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int maxNum = 1001;
        int[] count = new int[maxNum + 1];
        for (int i = 0; i < maxNum; i++) {
            count[i] = i;
        }

        int[] arr = new int[maxNum + 1];
        int cIdx = 1;
        for (int i = 1; i < maxNum; i++) {
            arr[i] = cIdx;
            count[cIdx]--;
            if (count[cIdx] == 0) {
                cIdx++;
            }
        }

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int answer = 0;
        for (int i = a; i <= b; i++) {
            answer += arr[i];
        }

        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}
