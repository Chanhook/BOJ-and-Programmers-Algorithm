import java.util.*;
class Solution {
    public int[] solution(String msg) {
        ArrayList<Integer> result = new ArrayList<>();
        ArrayList<String> dic = new ArrayList<>();
        
        for (int i = 0; i < 26; i++) {
            dic.add(String.valueOf((char)('A'+i)));
        }
        
        for (int i = 0; i < msg.length(); i++) {
            for (int j = dic.size()-1; j >= 0; j--) {
                if (msg.substring(i).startsWith(dic.get(j))) {
                    //다음 단어로 이동
                    i += dic.get(j).length()-1;
                    result.add(j+1);
                    if (i+1 < msg.length()) {
                        dic.add(dic.get(j)+msg.charAt(i+1));
                    }
                    break;
                }
            }
        }
        
        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        return answer;
    }
}