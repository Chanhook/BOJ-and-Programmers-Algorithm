import java.util.*;

class Solution {
    public String solution(int n, int t, int m, String[] timetable) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (String time : timetable) {
            pq.add(convertMin(time));
        }
        
        int start = convertMin("09:00");
        int lastTime = 0;
        int passenger = 0;
        for (int i = 0; i < n; i++) {
            passenger = 0;
            while (!pq.isEmpty()) {
                int curTime = pq.peek();
                //탈 수 있는 조건
                //1. curTime < start
                //2. passenger < m
                if (curTime <= start && passenger < m) {
                    pq.poll();
                    passenger++;
                } else break;
                lastTime = curTime - 1;
            }
            start += t;
        }
        
        //마지막 버스 m보다 작다면 탄다
        if (passenger < m) lastTime = start - t;
        
        return convertString(lastTime);
    }
    
    public int convertMin(String s) {
        int hour = Integer.parseInt(s.substring(0,2));
        int min = Integer.parseInt(s.substring(3));
        return hour * 60 + min;
    }
    
    public String convertString(int lastTime) {
        String hour = String.format("%02d", lastTime / 60);
        String minute = String.format("%02d", lastTime % 60);
        return hour + ":" + minute;
    }
}