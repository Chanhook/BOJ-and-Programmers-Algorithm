import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

  static int maxValue = -Integer.MAX_VALUE;
  static int minValue = Integer.MAX_VALUE;

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st;

    int n = Integer.parseInt(br.readLine());
    int[] arr = new int[n];

    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      int a = Integer.parseInt(st.nextToken());
      arr[i] = a;
    }

    st = new StringTokenizer(br.readLine());
    int[] operator = new int[4];
    for (int i = 0; i < 4; i++) {
      int a = Integer.parseInt(st.nextToken());
      operator[i] = a;
    }

    int aIdx = 1;
    recursive(arr, aIdx, arr[0], operator);

    bw.write(maxValue + "\n");
    bw.write(minValue + "\n");
    bw.flush();
    br.close();
    bw.close();
  }

  private static void recursive(int[] arr, int aIdx, int total, int[] operator) {
    if (aIdx == arr.length) {
      maxValue = Math.max(total, maxValue);
      minValue = Math.min(total, minValue);
      return;
    }

    for (int i = 0; i < 4; i++) {
      if (operator[i] > 0) {
        operator[i]--;
        if (i == 0) {
          recursive(arr, aIdx + 1, total + arr[aIdx], operator);
        } else if (i == 1) {
          recursive(arr, aIdx + 1, total - arr[aIdx], operator);
        } else if (i == 2) {
          recursive(arr, aIdx + 1, total * arr[aIdx], operator);
        } else {
          recursive(arr, aIdx + 1, total / arr[aIdx], operator);
        }
        operator[i]++;
      }
    }
  }

}
