class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                l = i + 1
                r = len(nums) - 1

                while l < r:
                    curr_sum = nums[i] + nums[l] + nums[r]
                    if curr_sum < 0:
                        l += 1
                    elif curr_sum > 0:
                        r -= 1
                    else:
                        triplets.append([nums[i], nums[l], nums[r]])
                        r -= 1
                        l += 1

                        while l < r and nums[l - 1] == nums[l]:
                            l += 1

        return triplets