import java.util.*;
class Solution {
    int[][] map1;
    int[][] map2;
    
    public static String toBinary(int n, int x) {
        return String.format("%" + n + "s", Integer.toBinaryString(x)).replaceAll(" ", "0");
    }
    
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        map1 = new int[n][n];
        map2 = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            int x = arr1[i];
            String bin = toBinary(n,x);
            for (int j = 0; j < n; j++) {
                map1[i][j] = bin.charAt(j) - '0';
            }
        }
        
        for (int i = 0; i < n; i++) {
            int x = arr2[i];
            String bin = toBinary(n,x);
            for (int j = 0; j < n; j++) {
                map2[i][j] = bin.charAt(j) - '0';
            }
        }
        
        char wall = '#';
        char blank = ' ';
        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < n; j++) {
                if (map1[i][j] == 0 && map2[i][j] == 0) {
                    sb.append(blank);
                } else {
                    sb.append(wall);
                }
            }
            answer[i] = sb.toString();
        }
        
        return answer;
    }
}