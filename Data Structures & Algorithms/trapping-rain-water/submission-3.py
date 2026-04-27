class Solution:
    def trap(self, height: List[int]) -> int:
        lp, rp = 0, len(height) - 1
        max_L, max_R = height[lp], height[rp]
        area = 0

        while lp < rp:
            if max_L <= max_R:
                # shift lp
                lp += 1
                # area += max(0, max_L - height[lp])
                max_L = max(max_L, height[lp])
                area += max_L - height[lp]
            else:
                # shift rp
                rp -= 1
                # area += max(0, max_R - height[rp])
                max_R = max(max_R, height[rp])
                area += max_R - height[rp]
        
        return area