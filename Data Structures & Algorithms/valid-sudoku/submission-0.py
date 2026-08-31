class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        for row in range(9):
            for col in range(9):
                row_box = row // 3
                col_box = col // 3
                box_number = row_box * 3 + col_box

                val = board[row][col] 
                if  val != ".":
                    if val in rows[row] or val in cols[col] or val in boxes[box_number]:
                        return False
                    else:
                        rows[row].add(val)
                        cols[col].add(val)
                        boxes[box_number].add(val)
        
        return True