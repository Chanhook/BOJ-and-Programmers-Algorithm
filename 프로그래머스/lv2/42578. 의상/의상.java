import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> map = new HashMap<>();
        for (String[] clothe : clothes) {
            map.put(clothe[1], map.getOrDefault(clothe[1], 0) + 1);
        }
        int answer = 1;
        for (String s : map.keySet()) {
            int cnt = map.get(s);
            answer *= (cnt + 1);
        }
        return answer - 1;
    }
}