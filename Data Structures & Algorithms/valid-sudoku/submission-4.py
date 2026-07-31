class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         seen = set()

         for i in range(9):
             for j in range(9):
                 value = board[i][j]

                 if value == ".":
                     continue

                 row = (value, "row", i)
                 col = (value, "col", j)
                 box = (value, "box", i // 3, j // 3)

                 if row in seen or col in seen or box in seen:
                     return False

                 seen.add(row)
                 seen.add(col)
                 seen.add(box)

         return True