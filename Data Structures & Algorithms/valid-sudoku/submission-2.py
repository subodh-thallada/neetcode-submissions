class Solution:

    def isInt(self,val):
        try:
            int(val)
            return True
        except:
            return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        counter_col = [set() for _ in range(9)]
        counter_sqr = [set() for _ in range(9)]
        for i in range(9):
            counter_row = set()
            for j in range(9):
                if self.isInt(board[i][j]):
                    if board[i][j] in counter_row:
                        return False
                    counter_row.add(board[i][j])

                    if board[i][j] in counter_col[j]:
                        return False
                    counter_col[j].add(board[i][j])

                    if 0<=j<=2:
                        if 0<=i<=2:
                            if board[i][j] in counter_sqr[0]:
                                return False
                            counter_sqr[0].add(board[i][j])
                        if 3<=i<=5:
                            if board[i][j] in counter_sqr[1]:
                                return False
                            counter_sqr[1].add(board[i][j])
                        if 6<=i<=8:
                            if board[i][j] in counter_sqr[2]:
                                return False
                            counter_sqr[2].add(board[i][j])

                    if 3<=j<=5:
                        if 0<=i<=2:
                            if board[i][j] in counter_sqr[3]:
                                return False
                            counter_sqr[3].add(board[i][j])
                        if 3<=i<=5:
                            if board[i][j] in counter_sqr[4]:
                                return False
                            counter_sqr[4].add(board[i][j])
                        if 6<=i<=8:
                            if board[i][j] in counter_sqr[5]:
                                return False
                            counter_sqr[5].add(board[i][j])

                    if 6<=j<=8:
                        if 0<=i<=2:
                            if board[i][j] in counter_sqr[6]:
                                return False
                            counter_sqr[6].add(board[i][j])
                        if 3<=i<=5:
                            if board[i][j] in counter_sqr[7]:
                                return False
                            counter_sqr[7].add(board[i][j])
                        if 6<=i<=8:
                            if board[i][j] in counter_sqr[8]:
                                return False
                            counter_sqr[8].add(board[i][j])

        return True