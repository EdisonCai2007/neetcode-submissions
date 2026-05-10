class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        lp, rp = 0, len(A) - 1
        while True:
            index_A = (lp + rp) // 2
            index_B = half - index_A - 2

            A_left = A[index_A] if index_A >= 0 else float("-infinity")
            A_right = A[index_A + 1] if index_A + 1 < len(A) else float("infinity")
            B_left = B[index_B] if index_B >= 0 else float("-infinity")
            B_right = B[index_B + 1] if index_B + 1 < len(B) else float("infinity")
            
            if B_left > A_right:
                lp = index_A + 1
            elif A_left > B_right:
                rp = index_A - 1
            else:
                # calculate median
                if total % 2 == 1:
                    return min(A_right, B_right)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2