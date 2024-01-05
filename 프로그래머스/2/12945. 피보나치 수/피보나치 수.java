class Solution {
    
    static int N = 1234567;
    
    public int solution(int n) {
        int[] fibo = new int[100001];
        fibo[0] = 0;
        fibo[1] = 1;
        
        for(int i = 2; i<=n; i++){
            fibo[i] = (fibo[i-1] % N + fibo[i-2] % N) % N;
        }
        
        return fibo[n];
        
    }
}