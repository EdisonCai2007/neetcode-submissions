class Solution {
    public int longestConsecutive(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>(); //<Number Needed : Size>
        HashSet<Integer> visited = new HashSet<>();

        int maxSize = 0;
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];

            if (!visited.contains(num)) {
                int newSize = map.getOrDefault(num-1,0) + map.getOrDefault(num+1,0) + 1;
                if (newSize > maxSize) maxSize = newSize;
                
                int rShift = map.getOrDefault(num+1,0);
                for (int j = 0; j < rShift; j++) {
                    map.put(num+1+j, newSize);
                }
                int lShift = map.getOrDefault(num-1,0);
                for (int j = 0; j < lShift; j++) {
                    map.put(num-1-j, newSize);
                }
                
                map.put(num, newSize);
            }

            visited.add(num);
        }

        return maxSize;
    }
}
