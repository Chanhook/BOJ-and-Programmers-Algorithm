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

        int[][] board = new int[H][W];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < W; i++) {
            int h = Integer.parseInt(st.nextToken());
            for (int j = 0; j < h; j++) {
                board[H - j - 1][i] = 1;
            }
        }

        int total = 0;
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (board[i][j] == 1) {
                    int count = 0;
                    boolean flag = false;
                    for (int k = j + 1; k < W; k++) {
                        if (board[i][k] == 0) {
                            count++;
                        } else if (board[i][k] == 1) {
                            flag = true;
                            break;
                        }
                    }
                    if (flag) {
                        total += count;
                    }
                }
            }
        }

        bw.write(total + "\n");
        bw.flush();
        br.close();
        bw.close();
    }
}