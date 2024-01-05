import java.util.Arrays;

public class Solution {
    private final int[][] mem = new int[101][101];

    private int count(int x, int y, int height, int width, boolean[][] isPuddle) {
        if (x > height || y > width) return 0;
        if (isPuddle[x][y]) return 0;
        if (mem[x][y] != -1) return mem[x][y];
        if (x == height && y == width) return 1;

        int total = count(x + 1, y, height, width, isPuddle)
                + count(x, y + 1, height, width, isPuddle);
        return mem[x][y] = total % 1000000007;
    }

    public int solution(int m, int n, int[][] puddles) {
        for (int[] row : mem) {
            Arrays.fill(row, -1);
        }

        boolean[][] isPuddle = new boolean[n + 1][m + 1];
        for (int[] p : puddles) {
            isPuddle[p[1]][p[0]] = true;
        }

        return count(1, 1, n, m, isPuddle);
    }
}
