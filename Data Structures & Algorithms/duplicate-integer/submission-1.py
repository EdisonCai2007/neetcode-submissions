class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occured = set()

        for num in nums:
            if num in occured:
                return True

            occured.add(num)
        
        return False