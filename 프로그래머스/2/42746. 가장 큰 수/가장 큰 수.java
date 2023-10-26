import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        List<Integer> list = new ArrayList<>();
        for (int number : numbers) {
            list.add(number);
        }

        list.sort((a, b) -> {
            String as = String.valueOf(a), bs = String.valueOf(b);
            return -Integer.compare(Integer.parseInt(as + bs), Integer.parseInt(bs + as));
        });

        StringBuilder sb = new StringBuilder();
        for (Integer number : list) {
            sb.append(String.valueOf(number));
        }

        if (sb.charAt(0) == '0') {
            return "0";
        } else {
            return sb.toString();
        }
    }
}