class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp, rp = 0, len(nums) - 1

        while lp < rp:
            mid = (lp + rp) // 2
            if target == nums[mid]: # target found
                return mid

            if nums[lp] <= nums[mid]: # in left-sorted portion
                if target > nums[mid]: 
                    lp = mid + 1
                else: # target < nums[mid]
                    if target < nums[lp]: 
                        lp = mid + 1
                    else: 
                        rp = mid - 1
            else: # in right-sorted portion
                if target < nums[mid]:
                    rp = mid - 1
                else: # target > nums[mid]
                    if target > nums[rp]:
                        rp = mid - 1
                    else:
                        lp = mid + 1
        
        return lp if target == nums[lp] else -1


# 3, 1
# l  r
# m