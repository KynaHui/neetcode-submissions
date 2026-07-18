class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each have 9 separate empty sets 
        # eg cols[2] == {"5", "8"}
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                grid_ind = (row // 3) * 3 + col // 3
                # see a repeat
                # grid[grid_ind]: check inside current box 
                if num in rows[row] or num in cols[col] or num in grid[grid_ind]:
                    return False
                rows[row].add(num)
                cols[col].add(num)
                grid[grid_ind].add(num)
        return True