class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapping = {}

        for i in range(len(nums)):
            if nums[i] in mapping:
                return [mapping[nums[i]], i]

            mapping[target - nums[i]] = i