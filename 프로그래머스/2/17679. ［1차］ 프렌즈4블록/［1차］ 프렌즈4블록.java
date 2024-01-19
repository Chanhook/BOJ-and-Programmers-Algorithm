import java.util.Arrays;

public class Solution {

    final char EMPTY = ' ';

    char[][] arr;
    boolean[][] visited;
    int height;
    int width;
    int total = 0;

    private boolean detect() {
        for (int i = 0; i < height - 1; i++) {
            for (int j = 0; j < width - 1; j++) {
                char target = arr[i][j];
                if (target == EMPTY) {
                    continue;
                }
                char right = arr[i][j + 1];
                char down = arr[i + 1][j];
                char diag = arr[i + 1][j + 1];
                if (target == right && target == down && target == diag) {
                    return true;
                }
            }
        }
        return false;
    }

    private void score() {
        visited = new boolean[height][width];
        for (boolean[] b : visited) {
            Arrays.fill(b, false);
        }

        for (int i = 0; i < height - 1; i++) {
            for (int j = 0; j < width - 1; j++) {
                char target = arr[i][j];
                if (target == EMPTY) {
                    continue;
                }
                char right = arr[i][j + 1];
                char down = arr[i + 1][j];
                char diag = arr[i + 1][j + 1];
                if (target == right && target == down && target == diag) {
                    visited[i][j] = true;
                    visited[i][j + 1] = true;
                    visited[i + 1][j] = true;
                    visited[i + 1][j + 1] = true;
                }
            }
        }

        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if (visited[i][j]) {
                    arr[i][j] = EMPTY;
                    total++;
                }
            }
        }
    }

    private void gravity() {
        char[][] temp = new char[height][width];
        for (int i = 0; i < height; i++) {
            Arrays.fill(temp[i], EMPTY);
        }

        for (int i = 0; i < width; i++) {
            int cur = height - 1;
            int tmp = cur;

            while (cur >= 0) {
                if (arr[cur][i] == EMPTY) {
                    cur--;
                    continue;
                }
                temp[tmp][i] = arr[cur][i];
                tmp--;
                cur--;
            }
        }

        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                arr[i][j] = temp[i][j];
            }
        }

    }

    public int solution(int m, int n, String[] board) {
        arr = new char[m][n];
        visited = new boolean[m][n];
        height = m;
        width = n;

        for (int i = 0; i < board.length; i++) {
            char[] row = board[i].toCharArray();
            for (int j = 0; j < row.length; j++) {
                arr[i][j] = row[j];
            }
        }

        while (detect()) {
            score();
            gravity();
        }

        return total;
    }
}