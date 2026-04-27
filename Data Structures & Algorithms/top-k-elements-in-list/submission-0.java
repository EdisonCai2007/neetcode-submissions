class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freq = new HashMap<>(); // Num : Freq
        HashMap<Integer, ArrayList<Integer>> count = new HashMap<>(); // Freq : [Num]

        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            freq.put(nums[i],freq.getOrDefault(nums[i],0)+1);

            if (freq.get(nums[i]) > max) max = freq.get(nums[i]);

            if (!count.containsKey(max)) count.put(max, new ArrayList<>());

            count.get(freq.get(nums[i])).add(nums[i]);
        }

        HashSet<Integer> uniqueAns = new HashSet<>();
        while (uniqueAns.size() < k) {
            for (int num : count.get(max)) {
                uniqueAns.add(num);
            }
            max--;
        }

        int[] ans = new int[k];
        int i = 0;
        for (int num: uniqueAns) {
            ans[i++] = num;
        }
        
        return ans;
    }
}


// [1,2,2,3,3,3]

// {1: [1,2,3]. 2: [2,3], 3: [3]}
