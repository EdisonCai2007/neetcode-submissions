class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lp, rp = 1, max(piles)

        while lp <= rp:
            mid = (lp + rp) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)

            # if eating time < target (eating too fast), slow down
            if time <= h:
                rp = mid - 1
            # if eating time > target (eating too slow), speed up
            elif time > h:
                lp = mid + 1

        return lp