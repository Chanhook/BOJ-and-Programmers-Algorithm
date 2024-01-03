import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        
        Queue<Integer> pq = new PriorityQueue<>();
        Queue<Integer> maxPq = new PriorityQueue<>(Collections.reverseOrder());
        
        for(String operation : operations) {
            StringTokenizer st = new StringTokenizer(operation);
            
            String req = st.nextToken();
            int value = Integer.parseInt(st.nextToken());
            
            if(pq.isEmpty() && req.equals("D")){
                continue;
            }
            
            if(req.equals("I")){
                pq.offer(value);
                maxPq.offer(value);
                continue;
            }
            
            if(value < 0){
                int min = pq.poll();
                maxPq.remove(min);
                continue;
            }
            
            int min = maxPq.poll();
            pq.remove(min);
        }
        
        if(pq.size() > 0 ) {
            answer[0] = maxPq.poll();
            answer[1] = pq.poll();
        }
        
        return answer;
    }
}