class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<Character> hs;

        for (char[] row : board) {
            hs = new HashSet<>();
            for (char c : row) {
                if (c != '.' && hs.contains(c)) {
                    return false;
                } else {
                    hs.add(c);
                }
            }
        }

        for (int i = 0; i < board[0].length; i++) { // iterate through all cols
            hs = new HashSet<>();
            for (int j = 0; j < board.length; j++) { // iterate thorugh all indexes within a col
                if (board[j][i] != '.' && hs.contains(board[j][i])) {
                    return false;
                } else {
                    hs.add(board[j][i]);
                }
            }
        }

        for (int i = 0; i < 9; i++) { // iterate thorugh all boxes
            hs = new HashSet<>();
            for (int j = 0; j < 3; j++) { // iterate through all rows
                for (int k = 0; k < 3; k++) { // iterate through all indexes within a row
                    int x = (i%3)*3 + k;
                    int y = (i/3)*3 + j;

                    if (board[y][x] != '.' && hs.contains(board[y][x])) {
                        return false;
                    } else {
                        hs.add(board[y][x]);
                    }
                }
            }
        }

        return true;
    }
}
