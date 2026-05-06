class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp, rp = 0, len(nums) - 1

        while lp < rp:
            mid = (lp + rp) // 2

            # if mid < both lp and rp, if so, move rp = mid 
            if nums[mid] < nums[lp] and nums[mid] < nums[rp]:
                rp = mid

            # if lp < rp, then rp = mid - 1
            elif nums[lp] < nums[rp]:
                rp = mid - 1

            # else rp < lp, then lp = mid + 1
            else: 
                lp = mid + 1
        
        return nums[lp]