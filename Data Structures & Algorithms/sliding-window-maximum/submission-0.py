class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # build first k-1 items with the deque
        dq = deque()
        for i in range(k-1):
            while len(dq) != 0 and dq[-1] < nums[i]:
                dq.pop()
            dq.append(nums[i])

        lp, rp = 0, k-1
        res = []

        while rp < len(nums):
            # add item at rp to the deque accordingly
            while len(dq) != 0 and dq[-1] < nums[rp]:
                dq.pop()
            dq.append(nums[rp])

            # get max in deque
            res.append(dq[0])

            # check lp is max and remove if needed
            if nums[lp] >= dq[0]:
                dq.popleft()
            # increment lp
            lp += 1

            # increment rp
            rp += 1

        return res

# [1,2,1,0,4,2,6]
# [^ ^ ^]    

# deque = 2, 1