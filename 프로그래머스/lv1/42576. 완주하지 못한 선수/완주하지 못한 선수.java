import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        Map<String, Integer> map= new HashMap<>();
        
        for(String p : participant){
            if(!map.containsKey(p)){
                map.put(p, 1);
                continue;
            }
            map.put(p, map.get(p)+1);
        }
        
        for(String c : completion){
            map.put(c, map.get(c)-1);
        }
        
        for(String k : map.keySet()){
            if(map.get(k)==1){
                answer = k;
            }
        }
        
        return answer;
    }
}