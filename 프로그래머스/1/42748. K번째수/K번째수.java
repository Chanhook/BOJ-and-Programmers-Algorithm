import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> ans = new ArrayList<>();

        for (int[] command : commands) {
            int s = command[0] - 1, e = command[1], idx = command[2] - 1;
            int[] subArray = Arrays.copyOfRange(array, s, e);
            Arrays.sort(subArray);
            ans.add(subArray[idx]);
        }

        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}