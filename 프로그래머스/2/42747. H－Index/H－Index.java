import java.util.*;
class Solution {
    public int binarySearchLower(int target, int[] arr) {
        int left = 0;
        int right = arr.length;

        while (left < right) {
            int mid = (left + right) / 2;
            if (target <= arr[mid]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    public int solution(int[] citations) {
        int answer = 0;

        Arrays.sort(citations);
        for (int i = citations[citations.length-1]; i > 0; i--) {
            int idx = binarySearchLower(i, citations);
            if (citations.length - idx >= i) {
                answer = i;
                break;
            }
        }

        return answer;
    }
}