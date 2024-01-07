import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.offer(n);
        int MAX = 100001;
        int[] visited = new int[MAX];
        visited[n] = 1;

        while (!queue.isEmpty()) {
            int x = queue.poll();
            if (x == k) {
                System.out.println(visited[x] - 1);
                break;
            }

            if (2 * x < MAX && visited[2 * x] == 0) {
                queue.offer(2 * x);
                visited[2 * x] = visited[x] + 1;
            }
            if (x - 1 >= 0 && visited[x - 1] == 0) {
                queue.offer(x - 1);
                visited[x - 1] = visited[x] + 1;
            }
            if (x + 1 < MAX && visited[x + 1] == 0) {
                queue.offer(x + 1);
                visited[x + 1] = visited[x] + 1;
            }
        }
    }
}
