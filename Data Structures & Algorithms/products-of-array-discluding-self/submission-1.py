class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        res = []

        for i in range(len(nums)):
            prod = 1
            for j in range(i+1, len(nums)):
                prod *= nums[j]
            
            res.append(prod * prev)
            prev *= nums[i]
        
        return res