class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        col=defaultdict(set)
        box=defaultdict(set)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                box_key=(i//3,j//3)

                if num in row[i] or num in col[j] or num in box[box_key]:
                    return False
                row[i].add(num)
                col[j].add(num)
                box[box_key].add(num)
        return True

        