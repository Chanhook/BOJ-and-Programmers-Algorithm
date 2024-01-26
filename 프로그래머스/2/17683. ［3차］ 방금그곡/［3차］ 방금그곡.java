class Solution {
    public String convert(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (i == s.length()-1) {
                sb.append(s.charAt(i));
                continue;
            }
            
            if (s.charAt(i+1) != '#') {
                sb.append(s.charAt(i));
            } else {
                sb.append(Character.toLowerCase(s.charAt(i)));
                i += 1;
            }
        }
        return sb.toString();
    }
    
    public String solution(String m, String[] musicinfos) {
        String answer = "(None)";
        int maxTime = 0;
        
        String convm = convert(m);
        
        for (String musicinfo : musicinfos) {
            String[] info = musicinfo.split(",");
            
            String[] start = info[0].split(":");
            int startTime = Integer.parseInt(start[0]) * 60 + Integer.parseInt(start[1]);
            
            String[] end = info[1].split(":");
            int endTime = Integer.parseInt(end[0]) * 60 + Integer.parseInt(end[1]);
            
            String title = info[2];
            
            String code = info[3];
            String convCode = convert(code);
            // System.out.println(code+" -> "+convCode);
            
            StringBuilder sb = new StringBuilder();
            int diff = endTime - startTime;
            int idx = 0;
            for (int i = 0; i < diff; i++) {
                idx %= convCode.length();
                sb.append(convCode.charAt(idx++));
            }
            String totalMusic = sb.toString();
            // System.out.println(totalMusic);
            
            if (totalMusic.contains(convm)) {
                if (diff > maxTime) {
                    maxTime = diff;
                    answer = title;
                }
            }
        }
        
        return answer;
    }
}