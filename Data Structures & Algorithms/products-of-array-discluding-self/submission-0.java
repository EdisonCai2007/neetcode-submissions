class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] pfx = new int[nums.length];
        int[] sfx = new int[nums.length];

        pfx[0] = nums[0];
        for (int i = 1; i < pfx.length; i++) {
            pfx[i] = pfx[i-1] * nums[i];
        }

        sfx[sfx.length-1] = nums[nums.length-1];
        for (int i = sfx.length-2; i >= 0; i--) {
            sfx[i] = sfx[i+1] * nums[i];
        }

        int[] ans = new int[nums.length];
        ans[0] = sfx[1];
        ans[ans.length-1] = pfx[pfx.length-2];
        for (int i = 1; i < nums.length-1; i++) {
            ans[i] = pfx[i-1] * sfx[i+1];
        }

        return ans;
    }
}  
