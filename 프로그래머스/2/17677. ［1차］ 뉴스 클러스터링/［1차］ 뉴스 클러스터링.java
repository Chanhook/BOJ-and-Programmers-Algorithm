import java.util.*;
class Solution {
    public static int solution(String str1, String str2) {
        HashSet<String> set = new HashSet<>();
        HashMap<String, Integer> map1 = new HashMap<>();
        HashMap<String, Integer> map2 = new HashMap<>();

        for (int i = 0; i < str1.length() - 1; i++) {
            String substring = str1.substring(i, i + 2).toLowerCase();
            if (Character.isAlphabetic(substring.charAt(0)) &&
                Character.isAlphabetic(substring.charAt(1))) {
                set.add(substring);
                map1.put(substring, map1.getOrDefault(substring, 0) + 1);
            }
        }

        for (int i = 0; i < str2.length() - 1; i++) {
            String substring = str2.substring(i, i + 2).toLowerCase();
            if (Character.isAlphabetic(substring.charAt(0)) &&
                Character.isAlphabetic(substring.charAt(1))) {
                set.add(substring);
                map2.put(substring, map2.getOrDefault(substring, 0) + 1);
            }
        }

        if (set.isEmpty()) {
            return 65536;
        }

        ArrayList<String> inter = new ArrayList<>();
        ArrayList<String> union = new ArrayList<>();

        for (String s : set) {
            if (map1.containsKey(s) && map2.containsKey(s)) {
                int count1 = map1.get(s);
                int count2 = map2.get(s);
                int min = Math.min(count1, count2);
                for (int i = 0; i < min; i++) {
                    inter.add(s);
                }
                int max = Math.max(count1, count2);
                for (int i = 0; i < max; i++) {
                    union.add(s);
                }
            } else {
                int count1 = map1.getOrDefault(s, 0);
                int count2 = map2.getOrDefault(s, 0);
                int max = Math.max(count1, count2);
                for (int i = 0; i < max; i++) {
                    union.add(s);
                }
            }

        }

        double jacade = (double) inter.size() / union.size();
        int answer = (int) (jacade * 65536);
        return answer;
    }
}