import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    static int STATION = 10;
    static int curPeople;
    static int maxPeople;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(out));
        StringTokenizer st;

        for (int i = 0; i < STATION; i++) {
            st = new StringTokenizer(br.readLine());
            int out = Integer.parseInt(st.nextToken());
            int in = Integer.parseInt(st.nextToken());
            curPeople = curPeople + in - out;
            if (curPeople > maxPeople) {
                maxPeople = curPeople;
            }
        }

        bw.write(maxPeople + "\n");
        bw.flush();
        br.close();
        bw.close();
    }

}
