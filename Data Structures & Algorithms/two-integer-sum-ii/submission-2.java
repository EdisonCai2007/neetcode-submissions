class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int pL = 0;
        int pR = numbers.length-1;

        while (numbers[pL] + numbers[pR] != target) {
            if (numbers[pL] + numbers[pR] > target) pR--;
            if (numbers[pL] + numbers[pR] < target) pL++;
        }

        return new int[]{pL+1,pR+1};
    }
}
