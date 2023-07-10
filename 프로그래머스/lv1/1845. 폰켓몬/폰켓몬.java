import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        Set<Integer> set = new HashSet<>();
        int pick = nums.length / 2;
        
        for(int num : nums){
            set.add(num);
        }
        
        int setSize = set.size();
        answer = Math.min(pick, setSize);
        
        return answer;
    }
}