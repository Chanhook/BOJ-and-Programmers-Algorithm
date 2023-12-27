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
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        int[] heights = new int[W];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < W; i++) {
            int h = Integer.parseInt(st.nextToken());
            heights[i] = h;
        }

        int total = 0;
        for (int i = 1; i < W - 1; i++) {
            int curHeight = heights[i];

            int leftMaxHeight = -1;
            for (int j = 0; j < i; j++) {
                if (heights[j] > leftMaxHeight) {
                    leftMaxHeight = heights[j];
                }
            }

            int rightMaxHeight = -1;
            for (int j = i + 1; j < W; j++) {
                if (heights[j] > rightMaxHeight) {
                    rightMaxHeight = heights[j];
                }
            }

            int maxHeight = Math.min(leftMaxHeight, rightMaxHeight);
            if (maxHeight > curHeight) {
                total += maxHeight - curHeight;
            }
        }
        bw.write(total + "\n");
        bw.flush();
        br.close();
        bw.close();
    }
}