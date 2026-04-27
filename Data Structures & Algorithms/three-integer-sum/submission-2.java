class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        
        Arrays.sort(nums);
        for (int i = 0; i < nums.length-1; i++) {
            if (i == 0 || nums[i-1] != nums[i]) {
                int lP = i + 1;
                int rP = nums.length-1;

                while (lP < rP) {
                    if (nums[lP] + nums[rP] == -nums[i]) {
                        ans.add(new ArrayList<>(Arrays.asList(nums[i],nums[lP],nums[rP])));
                        lP++;
                        while(nums[lP] == nums[lP-1] && lP < rP) {
                            lP++;
                        }
                    }
                    if (nums[lP] + nums[rP] > -nums[i]) rP--;
                    if (nums[lP] + nums[rP] < -nums[i]) lP++;
                }
            }
        }

        return ans;
    }
}
