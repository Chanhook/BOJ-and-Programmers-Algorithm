import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 0;
        String item = "";
        String category = "";
        
        Map<String, List<String>> clothMap = new HashMap<>();
        
        for(String[] cloth : clothes) {
            item = cloth[0];
            category = cloth[1];
            
            if (!clothMap.containsKey(category)) {
                clothMap.put(category, new ArrayList<>());
            }
            
            clothMap.get(category).add(item);
        }
        
        int combi = 1;
        for (String key : clothMap.keySet()) {
            combi *= clothMap.get(key).size() + 1;
        }
        answer = combi - 1;
        
        return answer;
    }
}