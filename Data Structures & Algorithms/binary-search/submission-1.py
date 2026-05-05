class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp, rp = 0, len(nums)-1

        while lp < rp:
            mid = (lp + rp) // 2
            if nums[mid] < target:
                lp = mid + 1
            elif nums[mid] > target:
                rp = mid - 1
            else:
                return mid
        
        return lp if nums[lp] == target else -1
