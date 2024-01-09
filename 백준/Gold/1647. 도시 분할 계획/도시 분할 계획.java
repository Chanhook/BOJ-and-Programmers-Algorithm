import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    static int n, m;
    static int[] parent;
    static ArrayList<Node> graph = new ArrayList<>();

    static int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    static void union(int x, int y) {
        int a = find(x);
        int b = find(y);
        if (a < b) {
            parent[b] = a;
        } else {
            parent[a] = b;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        parent = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int distance = Integer.parseInt(st.nextToken());
            graph.add(new Node(start, end, distance));
        }

        Collections.sort(graph);

        int result = 0;
        int prev = 0;
        for (Node node : graph) {
            int a = node.getStart();
            int b = node.getEnd();
            int distance = node.getDistance();
            if (find(a) != find(b)) {
                union(a, b);
                result += distance;
                prev = distance;
            }
        }

        bw.write(result - prev + "\n");
        bw.flush();
        br.close();
        bw.close();
    }

    static class Node implements Comparable<Node> {

        int start;
        int end;
        int distance;

        public Node(int start, int end, int distance) {
            this.start = start;
            this.end = end;
            this.distance = distance;
        }

        public int getStart() {
            return start;
        }


        public int getEnd() {
            return end;
        }

        public int getDistance() {
            return distance;
        }


        @Override
        public int compareTo(Node o) {
            return this.distance - o.distance;
        }
    }

}
