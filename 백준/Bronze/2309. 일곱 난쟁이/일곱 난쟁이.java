import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(out));

        int n = 9;
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Set<Integer> selectedDwarfs = null;

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                Set<Integer> set = new HashSet<>();
                for (int k = 0; k < n; k++) {
                    if (k != i && k != j) {
                        set.add(arr[k]);
                    }
                }
                if (set.stream().mapToInt(Integer::intValue).sum() == 100 && set.size() == 7) {
                    selectedDwarfs = set;
                    break;
                }
            }
            if (selectedDwarfs != null) {
                break;
            }
        }

        // Set을 ArrayList으로 변환하여 오름차순 정렬
        List<Integer> sortedDwarfs = new ArrayList<>(selectedDwarfs);
        Collections.sort(sortedDwarfs);

        // 정렬된 값을 한 줄 씩 출력
        if (sortedDwarfs != null) {
            for (int dwarf : sortedDwarfs) {
                bw.write(dwarf + "\n");
            }
        }

        bw.flush();
        br.close();
        bw.close();

    }
}
