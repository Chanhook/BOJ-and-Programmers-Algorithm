import java.util.*;
class Solution {
    ArrayList<File> arr = new ArrayList<>();
    
    public String[] solution(String[] files) {
        StringBuilder sb;
        int h = 0;
        int n = 0;
        int t = 0;    
        for (String file : files) {
            sb = new StringBuilder();
            n = 0;
            t = file.length();
            
            for (int i = 0; i < file.length(); i++) {
                char ch = file.charAt(i);
                if (Character.isDigit(ch)) {
                    n = i;
                    break;
                }
                sb.append(ch);
            }
            String head = sb.toString();
            
            
            sb = new StringBuilder();
            for (int i = n; i < file.length(); i++) {
                char ch = file.charAt(i);
                if (!Character.isDigit(ch)) {
                    t = i;
                    break;
                }
                sb.append(ch);
            }
            String number = sb.toString();
            
            String tail = file.substring(t);
            
            arr.add(new File(head, number, tail));
        }
        
        Collections.sort(arr);
        
        String[] answer = new String[files.length];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = arr.get(i).getFileName();
        }
        return answer;
    }
}

class File implements Comparable<File>{
    String head;
    String compHead;
    String number;
    int compNumber;
    String tail;
    
    File (String head, String number, String tail) {
        this.head = head;
        this.compHead = head.toUpperCase();
        this.number = number;
        this.compNumber = Integer.parseInt(number);
        this.tail = tail;
    }
    
    public String getFileName() {
        return head+number+tail;
    }
    
    @Override
    public int compareTo(File o) {
        // compHead 비교 (사전순으로 오름차순)
        int headComparison = this.compHead.compareTo(o.compHead);

        if (headComparison != 0) {
            return headComparison;
        }

        // compNumber 비교 (숫자 오름차순)
        return Integer.compare(this.compNumber, o.compNumber);
    }
    
}