import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    static int MAX = 100001;
    static int n, k;
    static int[] visited = new int[MAX];
    static int[] parent = new int[MAX];


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        int time = bfs(n, k);

        Stack<Integer> stack = new Stack<>();
        stack.push(k);
        int idx = k;
        while (idx != n) {
            stack.push(parent[idx]);
            idx = parent[idx];
        }

        System.out.println(time);
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()){
            sb.append(stack.pop()).append(" ");
        }
        System.out.println(sb);
    }

    private static int bfs(int n, int k) {
        LinkedList<Integer> queue = new LinkedList<>();
        queue.offer(n);
        visited[n] = 1;

        int x;
        while (!queue.isEmpty()) {
            x = queue.poll();
            if (x == k) {
                break;
            }

            if (2 * x < MAX && visited[2 * x] == 0) {
                queue.offer(2 * x);
                visited[2 * x] = visited[x] + 1;
                parent[2 * x] = x;
            }
            if (x - 1 >= 0 && visited[x - 1] == 0) {
                queue.offer(x - 1);
                visited[x - 1] = visited[x] + 1;
                parent[x - 1] = x;
            }
            if (x + 1 < MAX && visited[x + 1] == 0) {
                queue.offer(x + 1);
                visited[x + 1] = visited[x] + 1;
                parent[x + 1] = x;
            }
        }
        return visited[k] - 1;
    }
}
