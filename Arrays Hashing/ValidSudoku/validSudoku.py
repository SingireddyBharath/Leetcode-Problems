# O(9^2) time complexity   and space complexity

import collections

def isValidSudoku(board) -> bool:
        
        cols=collections.defaultdict(set)     # key is row number
        rows=collections.defaultdict(set)     # key is cols number
        squares=collections.defaultdict(set)  # key is (row//3.cols//3)
        
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if (board[r][c] in cols[c] or 
                    board[r][c] in rows[r] or 
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])

                squares[(r//3,c//3)].add(board[r][c])            
            
        return True