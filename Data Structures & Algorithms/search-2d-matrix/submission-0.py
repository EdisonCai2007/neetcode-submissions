class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lp, rp = 0, m * n - 1

        while lp < rp:
            mid = (lp + rp) // 2

            # if mid is less than target, move lp
            if matrix[mid // n][mid % n] < target:
                lp = mid + 1
            # if mid is greater than target, move rp
            elif matrix[mid // n][mid % n] > target:
                rp = mid - 1
            # else, target found -> return true
            else:
                return True

        return True if matrix[lp // n][lp % n] == target else False
        