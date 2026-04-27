class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp, rp = 0, len(heights) - 1
        maximum = 0

        while lp < rp:
            area = min(heights[lp], heights[rp]) * (rp - lp)
            if area > maximum:
                maximum = area

            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1

        return maximum