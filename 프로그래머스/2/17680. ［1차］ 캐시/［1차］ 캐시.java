import java.util.LinkedHashMap;
import java.util.Map;

public class Solution {

    class Cache<String, Integer> extends LinkedHashMap<String, Integer> {

        int capacity = 0;

        public Cache(int capacity) {
            super(capacity, 0.75f, true);
            this.capacity = capacity;
        }

        @Override
        protected boolean removeEldestEntry(Map.Entry<String, Integer> eldest) {
            // eldest 가장 오랫동안 안쓴 데이터
            return size() > capacity;
        }
    }

    public int solution(int cacheSize, String[] cities) {
        if (cacheSize == 0) {
            return 5 * cities.length;
        }

        int time = 0;

        Cache<String, Integer> cache = new Cache<String, Integer>(cacheSize);

        for (String city : cities) {
            String lowerCase = city.toLowerCase();
            if (!cache.containsKey(lowerCase)) {
                time += 5;
            } else {
                time += 1;
            }
            cache.put(lowerCase, 0);
        }

        return time;
    }
}
