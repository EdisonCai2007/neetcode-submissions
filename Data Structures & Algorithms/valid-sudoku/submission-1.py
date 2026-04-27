class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            if self.checkDuplicates(board[i]):
                return False
        
        for i in range(len(board[0])):
            col = []
            for j in range(len(board)):
                col.append(board[j][i])
            
            if self.checkDuplicates(col):
                return False
        
        for box in range(9):
            grid = []
            for i in range(box % 3 * 3, box % 3 * 3 + 3):
                for j in range(box // 3 * 3, box // 3 * 3 + 3):
                    grid.append(board[i][j])

            if self.checkDuplicates(grid):
                return False

        return True            

    def checkDuplicates(self, nums: list[str]) -> bool:
        seen = set()
        for num in nums:
            if num != '.':
                if num not in seen:
                    seen.add(num)
                else:
                    return True

        return False