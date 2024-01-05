class Solution {
    public String solution(String s, int n) {
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (!Character.isAlphabetic(ch)) {
                sb.append(ch);
                continue;
            }
            
            
            int offset = Character.isUpperCase(ch) ? 'A' : 'a';
            // A 65 a 97
            int position = ch - offset;
            position = (position + n) % ('Z'-'A'+1);
            sb.append((char)(offset+position));        
        }
        return sb.toString();
    }
}