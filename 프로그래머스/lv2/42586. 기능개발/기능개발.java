import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> q = new ArrayDeque<>();
        List<Integer> list = new ArrayList<>();
        
        for(int i = 0; i < speeds.length; i++){
            double remain = (100-progresses[i])/(double) speeds[i];
            int date = (int) Math.ceil(remain);
            if(!q.isEmpty() && q.peek()<date){
                list.add(q.size());
                q.clear();
            }
            q.offer(date);
        }
        
        list.add(q.size());
        
        return list.stream().mapToInt(Integer::intValue).toArray();
            
    }
}